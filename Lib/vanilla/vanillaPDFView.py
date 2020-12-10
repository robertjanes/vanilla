from AppKit import PDFDocument, NSURL, NSEdgeInsets
from AppKit import PDFView as AppKitPDFView
from vanilla.vanillaBase import VanillaBaseObject
import os


class PDFView(VanillaBaseObject):

    """
    A PDF view

    ::
        from vanilla import Window, PDFView

        class PDFViewDemo:

            def __init__(self):
                self.w = Window((600, 600))
                self.w.PDFView = PDFView((0, 0, 0, 0))
                self.w.PDFView.setDocumentWithPath("/path/to/file.pdf")
                self.w.open()

        PDFViewDemo()

    **posSize** Tuple of form *(left, top, width, height)* or *"auto"* representing
    the position and size of the scroll view.

    """

    nsPDFViewClass = AppKitPDFView

    def __init__(self, posSize):
        self._setupView(self.nsPDFViewClass, posSize)

    def setDocument(self, document=None):
        if document is not None:
            self._nsObject.setDocument_(document)
        else:
            raise ValueError("No PDF Document defined")

    def setDocumentWithPath(self, path=None):
        if path is not None:
            path = os.path.abspath(os.path.expanduser(path))
            self.documentURL = NSURL.alloc().initFileURLWithPath_(path)
        else:
            raise ValueError("No PDF source defined")
        self.document = PDFDocument.alloc().initWithURL_(self.documentURL)
        self.setDocument(self.document)

    def setDisplayMode(self, modeInt):
        self._nsObject.setDisplayMode_(modeInt)

    def setBackgroundColor(self, color):
        self._nsObject.setBackgroundColor_(color)

    def setDisplayDirection(self, PDFDisplayDirection):
        self._nsObject.setDisplayDirection_(PDFDisplayDirection)

    def setPageBreakMargins(m):
        self._nsObject.setPageBreakMargins_(NSEdgeInsets(m[0], m[1], m[2], m[3]))

    def goBack(self):
        self._nsObject.goBack_(None)

    def goForward(self):
        self._nsObject.goForward_(None)

    def goToFirstPage(self):
        self._nsObject.goToFirstPage_(None)

    def goToLastPage(self):
        self._nsObject.goToLastPage_(None)

    def goToNextPage(self):
        self._nsObject.goToNextPage_(None)

    def goToPreviousPage(self):
        self._nsObject.goToPreviousPage_(None)

    def goToPage(self, n):
        PDFPage = self.document.pageAtIndex_(n)
        self._nsObject.goToPage_(PDFPage)
