
## A Harvard-specific Django LTI app
**that allows course authors to insert their old course information into
the Canvas Rich Content Editor as formatted text, or as a live-updating widget.**

Authors click an icon, which opens an editor window to let him/her choose
which fields he/she would like to include, and whether to insert them as editable
text, or as a widget.

## See the docs directory for instructions on how to run this app locally and in Heroku.

In order for the iframes to size properly, you'll have to add the following snippet to your canvas global js file:

course_info/static/js/consumer/global.js

It's annoying that this is necessary, but that's the way things are with cross-domain iframes.


### A Note on oEmbed:
**(www.oembed.com)**

The Canvas Rich Content Editor can be rather unforgiving at the margin.
You can insert links, videos, iFrames, and images rather easily. However
inserting editable, custom, rich content such as blocks of generated HTML is a bit more involved.

To do this you need to use/implement the oEmbed protocol.
At its core, your launch app must send Canvas three values (implemented as inputs in this app):

```
the return_type (which will be oembed)
the endpoint: the oembed_location (more on this in a bit)
the url: some dynamic query url
```

the "url" could more aptly be named the "parameters" - what Canvas does is concatenate the url
onto the endpoint, and then send that request out from their servers. This means that
**you must have a live server to develop with oEmbed.**

Using another site's oEmbed API is rather straightforward - they've implemented it.
Just insert their endpoint (the designated oembed path -- for example: http://www.twitter.com/oembed)
and the desired query url (for example http://www.twitter.com/Jack/status/20)

A full oEmbed submission setup (to Canvas, from Twitter, through your app) would look like the HTML below:

    <input type="hidden"   name="return_type"  value="oembed"/>
    <input type="hidden"   name="endpoint"     value="https://api.twitter.com/1/statuses/oembed.json?"/>
    <input type="hidden"   name="url"          value="https://twitter.com/Jack/status/20"/>

The query Canvas would send out after it received those inputs would be as follows:
https://api.twitter.com/1/statuses/oembed.json?url=https://twitter.com/Jack/status/20

Notice the insertion of "url="  --  the full url is included as a query parameter.
For all intents and purposes, the fact that it's a url is irrelevant, though customary.

**The above example shows a proper implementation of oEmbed. Understanding it makes the steps
for a developer to insert his/her own rich content into Canvas' editor somewhat clearer.
Here's what it boils down to:**

You'll need an LTI launch, which sends Canvas to the
'endpoint' path, with the 'url' parameter. This endpoint path should be a view that you
have programmed to respond to such a request.
oEmbed must return either XML or JSON, with "type" and "html" objects.

For example, the following oEmbed-like JSON could be sent back to Canvas from your Django view:

```python
response_json = json.JSONEncoder().encode({
	"html": "\<p\>I'm Like Hey What's Up Hello\</p\>",
	"type": "rich"
});

return HttpResponse(response_json, content_type="application/json")
```

####See the oembed_handler view in "course_info/views.py" for an example of an oEmbed implementation
