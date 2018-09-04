#-*- coding:utf-8 -*-

import wx

class DemoFrame( wx.Frame ):
    def __init__( self, parent=None, id=wx.ID_ANY, title=u'wxPython Study', size=(800,600) , style=wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__( self, parent=parent, id=id, title=title, size=size, style=style )

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.CenterOnParent()
    frame.Show()
    app.MainLoop()
