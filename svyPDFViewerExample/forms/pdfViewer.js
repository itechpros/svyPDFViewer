/**
 * @type {String}
 *
 * @properties={typeid:35,uuid:"FAAAC345-AD6E-4068-8F2F-D4653BCCE0AB"}
 */
var documentURL = '';


/**
 * Handle changed data, return false if the value should not be accepted. In NGClient you can return also a (i18n) string, instead of false, which will be shown as a tooltip.
 *
 * @param {String} oldValue old value
 * @param {String} newValue new value
 * @param {JSEvent} event the event that triggered the action
 *
 * @return {Boolean}
 *
 * @private
 *
 * @properties={typeid:24,uuid:"FAAFF2F3-46FE-4FD6-9C4B-55EF13903824"}
 */
function onDataChange(oldValue, newValue, event) {
	elements.pdfViewer.documentURL = documentURL;
	return true
}

/**
 * Callback method when form is (re)loaded.
 *
 * @param {JSEvent} event the event that triggered the action
 *
 * @private
 *
 * @properties={typeid:24,uuid:"887EC2E2-4FF8-4D8F-9FA2-DFA5A12C1B61"}
 */
function onLoad(event) {
//	elements.pdfViewer.setDocument(documentURL);
	elements.pdfViewer.documentURL = 'test.pdf';
}
