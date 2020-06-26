{
	"name": "pdfviewer-pdf-Viewer",
	"displayName": "pdfViewer",
	"categoryName": "Media",
	"version": 1,
	"icon": "pdfviewer/pdfViewer/icon.png",
	"definition": "pdfviewer/pdfViewer/pdfViewer.js",
	"libraries": [],
	"model":
	{
        "documentURL"   : {"type" : "string"},
        "dataProviderID": {"type":"dataprovider", "tags": { "scope" :"design" }},
        "styleClass"    :   {"type" :"styleclass", "tags": { "scope" :"design" }},
		"noCache" 		: {"type" : "boolean"},
		"visible"       : {"type": "visible" },
		"size"          : {"type": "dimension",  "default" : {"width":100, "height":40}}
	},
	"api" : 
	{
		"reload" : {
            "delayUntilFormLoads": true 
        }
	}
}