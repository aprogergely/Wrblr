import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,300))

        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 3, 20, 20)
		
        button = wx.Button(panel, label = "Go")

        self.searchField = wx.TextCtrl(panel)
        self.saveField = wx.TextCtrl(panel)
        self.deleteField = wx.TextCtrl(panel)
        self.searchField.SetHint("Keres")
        self.saveField.SetHint("Tárol")
        self.deleteField.SetHint("Töröl")

        self.outputField = wx.StaticText(panel)

        button.Bind(wx.EVT_BUTTON, self.OnClick)

        fgs.AddMany([wx.StaticText(panel, label = ""), button, wx.StaticText(panel, label = ""), 
                     self.searchField, self.saveField, self.deleteField, wx.StaticText(panel, label = ""),
                     self.outputField, wx.StaticText(panel, label = "")] )
        
        hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15) 
        
        panel.SetSizer(hbox)

        self.Show(True)

    def OnClick(self, e):
        toSearch = self.searchField.GetValue()
        toSave = self.saveField.GetValue()
        toDelete= self.deleteField.GetValue()

        with open('database.txt', 'a') as f:
            f.write(toSave + "\n")

        with open('database.txt', 'r') as f:
            data = f.read()
            if toSearch:
                if data.find(toSearch): 
                    self.outputField.SetLabelText("Benne van")
                else:
                    self.outputField.SetLabelText("Nincs benne")
            else:
                self.outputField.SetLabelText("")


        lines = []
        with open("database.txt", 'r') as f:
            lines = f.readlines()

        with open("database.txt", 'w') as f:
            for line in lines:
                if line.strip("\n") != toDelete:
                    f.write(line)

app = wx.App(False)
frame = Example(None, 'Example')
app.MainLoop()