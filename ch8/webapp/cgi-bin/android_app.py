#!/usr/bin/python3
import android

app = android.Android()

app.dialogCreateAlert("Select an athlete:")
app.dialogSingleChoiceItems(["Mikey","Sarah","James","Julie"])
app.dialogSetPositiveButtonText("Select")
app.dialogSetNegativeButtonText("Quit")
app.dialogShow()
resp = app.dialogGetResponse().result
