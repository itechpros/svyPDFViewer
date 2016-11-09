{
	"name": "pdfviewer-pdf-Viewer",
	"displayName": "pdfViewer",
	"version": 1,
	"definition": "pdfviewer/pdfViewer/pdfViewer.js",
	"libraries": [
		{"name":"pdf.js","version":"1", "url":"pdfviewer/pdfViewer/build/pdf.js", "mimetype":"text/javascript"},
		{"name":"pdf.worker.js","version":"1", "url":"pdfviewer/pdfViewer/build/pdf.worker.js", "mimetype":"text/javascript"},
		{"name":"viewer.html","version":"1", "url":"pdfviewer/pdfViewer/web/viewer.html", "mimetype":"text/html"},
		{"name":"viewer.js","version":"1", "url":"pdfviewer/pdfViewer/web/viewer.js", "mimetype":"text/javascript"},
		{"name":"viewer.css","version":"1", "url":"pdfviewer/pdfViewer/web/viewer.css", "mimetype":"text/css"}
	],
	"model":
	{
		"documentURL" : {"type": "string"}
	},
	"handlers" : {},
	
	"api" : 
	{
		"setDocument" :
		{
			"parameters" : [
				{ "name" : "url", "type" : "string" }
			]
		}
	}
}