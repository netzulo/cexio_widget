#!/usr/bin/python
# -*- coding: utf-8 -*-

# absolute.py

import wx, requests, time, json

class BaseFrame(wx.Frame):
  
    def __init__(self, parent, title):
        super(BaseFrame, self).__init__(parent, title=title, size=(200, 70), style=wx.NO_BORDER | wx.STAY_ON_TOP)
                    
        self.InitUI()
        
    def InitUI(self):    
        self.panel = wx.Panel(self, -1)

        menubar = wx.MenuBar()
        filem = wx.Menu()
        helpm = wx.Menu()

        menubar.Append(filem, '&CEX')
        menubar.Append(helpm, '&Donate')
        self.SetMenuBar(menubar)
        # Load DATA
        self.OnReload()

    def OnReload(self):
        main_btc_eur = wx.StaticText(self.panel, pos=(5,0), style=wx.ALIGN_LEFT)
        main_btc_eur.SetLabel("{}: {}".format("BTCEUR", requests.get("https://cex.io/api/last_price/BTC/EUR").json()['lprice']))
        main_btc_usd = wx.StaticText(self.panel, pos=(5,20), style=wx.ALIGN_LEFT)
        main_btc_usd.SetLabel("{}: {}".format("BTCUSD", requests.get("https://cex.io/api/last_price/BTC/USD").json()['lprice']))

        time.sleep(1)
        wx.CallLater(1000,self.OnReload)


if __name__ == '__main__':
  
    app = wx.App()
    frame = BaseFrame(None, title='')
    frame.Show()
    app.MainLoop()
