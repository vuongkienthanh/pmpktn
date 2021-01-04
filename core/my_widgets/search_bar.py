from initialize import *
import other_func as otf

import wx


class PatientSearchBar(wx.TextCtrl):

    def __init__(self, parent):
        super().__init__(parent)
        self.mv = parent
        self.SetHint("Tìm kiếm bệnh nhân")
        self.set_timer()

    def set_timer(self):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_search)
        self.Bind(wx.EVT_TEXT, self.on_text)

    def filter_patient(self, p_list):
        return filter(lambda p: self.Value.upper() in p.name, p_list)

    def on_text(self, e):
        if self.Value != "":
            self.timer.StartOnce(setting["time_between_search"])
        else:
            self.mv.patient_book.GetPage(0)._append()

    def on_search(self, e):
        patient_book = self.mv.patient_book.GetPage(0)
        filtered_p_list = self.filter_patient(patient_book.p_list)
        patient_book.DeleteAllItems()
        for p in filtered_p_list:
            b = otf.bd_to_age(p.birthdate)
            patient_book.Append([
                p.id, p.name, p.gender, b])
