import wx
from pynput.keyboard import Key, Listener
import threading

from ctypes import windll

# get the handle to the taskbar
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

# hide the taskbar
windll.user32.ShowWindow(h, 0)


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        self.InitFrame()

    def InitFrame(self):
        self.title = "Launch Viewer:New"
        self.frame=MyFrame(parent=None,title=self.title)
        self.frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent,title):
        style = (wx.NO_BORDER|wx.FRAME_SHAPED)
        super().__init__(parent=parent,title=title,style=style,size=(256,256),pos=(1659,5))
        self.SetTransparent(150)

        panel = firstPanel(parent=self)


        self.popupmenu = wx.Menu()
        quit = self.popupmenu.Append(-1,"quit")
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)

        self.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)

    def OnShowPopup(self, event):
        pos = event.GetPosition()
        pos = self.ScreenToClient(pos)
        self.PopupMenu(self.popupmenu, pos)


    def OnQuit(self, event):
        self.Close()



class firstPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent,size=(256,256))


        self.SetBackgroundColour("black")

        self.imageCtrl = wx.StaticBitmap(self)


        self.initfram()
        t = threading.Thread(target=self.keyrecode)
        t.start()


    def on_press(self,key):
        if self.count%2 == 0:
            self.imageCtrl.SetBitmap(wx.Bitmap(self.img_left))
            self.count += 1
            self.Refresh()

        else:
            self.imageCtrl.SetBitmap(wx.Bitmap(self.img_right))
            self.count += 1
            self.Refresh()


    def on_release(self,key):
        self.imageCtrl.SetBitmap(wx.Bitmap(self.img))
        self.Refresh()
        
    def initfram(self):
        path = "hands_up.jpg"
        #img = wx.EmptyImage(240,240)
        self.img = wx.Image(path,wx.BITMAP_TYPE_ANY)
        self.img_left = wx.Image("hands_left.jpg",wx.BITMAP_TYPE_ANY)
        self.img_right = wx.Image("hands_right.jpg",wx.BITMAP_TYPE_ANY)

        self.count = 0

        self.imageCtrl.SetBitmap(wx.Bitmap(self.img))
        self.Refresh()


    def keyrecode(self):

        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
