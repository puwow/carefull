#-*- coding:utf-8 -*-

import wx

class BookPage( wx.Panel ):
    def __init__( self, parent, id=wx.ID_ANY ):
        wx.Panel.__init__( self, parent=parent, id=id )

class DemoFrame( wx.Frame ):
    def __init__( self, parent=None, id=wx.ID_ANY, title=u'wxPython Study', size=(800,600) , style=wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__( self, parent=parent, id=id, title=title, size=size, style=style )
        panel = wx.Panel( self, id=wx.ID_ANY )
        box = wx.BoxSizer( wx.VERTICAL )
        book = wx.Notebook( panel, id=wx.ID_ANY )
        page1 = BookPage(book)
        page2 = BookPage(book)
        page3 = BookPage(book)
        book.AddPage( page1, u'页面1' )
        book.AddPage( page2, u'页面2' )
        book.AddPage( page3, u'页面5' )
        box.Add( book, 1, wx.EXPAND|wx.ALL, 3 )

        panel.SetSizer( box )

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.CenterOnParent()
    frame.Show()
    app.MainLoop()
