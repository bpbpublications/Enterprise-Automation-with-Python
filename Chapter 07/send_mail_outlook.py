import sys
import os
import argparse
import csv
import win32com.client

ol = win32com.client.DispatchEx("Outlook.Application")
Msg = ol.CreateItem(0)
Msg.To = "pyemailtestautomation@gmail.com"
Msg.Subject = "Automation Bot"
Msg.Send()
print("Email sent")
ol.Quit()
