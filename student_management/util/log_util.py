consoleLogText = ""
textEditWidget = None

OutputLogText = ""
textOutputWidget = None

def SetConsoleLogTarget(logTextWidget):
    global textEditWidget
    textEditWidget = logTextWidget

def WriteConsoleLog(log):
    global consoleLogText, textEditWidget
    consoleLogText = log + "\n"
    #print(log)
    textEditWidget.append(consoleLogText)

def SetOutputLogTarget(logTextWidget):
    global textOutputWidget
    textOutputWidget = logTextWidget

def WriteOutputLog(log):
    global OutputLogText, textOutputWidget
    OutputLogText = log + "\n"
    #print(log)
    textOutputWidget.append(OutputLogText)