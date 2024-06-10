import re
import pandas as pd
def openexel(fileName):
    df = pd.read_excel(fileName)
    return df
def writedf(df:pd.DataFrame, num):
    df.to_excel("output"+str(num)+".xlsx", startcol=0, index=False)
def readTransformWrite():
    globalid=0
    for i in range(1,4):
        df = openexel(str(i)+".xlsx")
        df = df.assign(id = range(globalid, globalid+len(df)))
        print(df)
        globalid+=len(df)
        writedf(df,i)
