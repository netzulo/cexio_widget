import wx,json,requests,time
class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('Title')
        panel = wx.Panel(self)
        style = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE
        self.text = wx.StaticText(panel, style=style)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(self.text, 0, wx.EXPAND)
        sizer.AddStretchSpacer(1)
        panel.SetSizer(sizer)
        self.on_timer()
    def on_timer(self):
        myData = requests.get('https://cex.io/api/last_price/BTC/USD')
        myRealData = myData.json()
        x = myRealData['lprice']
        print x
        self.text.SetLabel(str(x))
        time.sleep(1)
        wx.CallLater(1000, self.on_timer)
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
