# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:20:41 2020

@author: Administrator
"""

"""变量命名准则文件"""
"""所有变量都必须以basic_string中的字符串结尾，且中间部分不含basic_string中的字符串"""
basic_strings = ["Open","High","Low","Close",
                "Volume","Vwap","Avg","Status",
                "Pb","Reason","Value","Amount","Rate",
                "I000010","I000016","I000019","I000021",
                 "I000160","I000300","I000905","I000906",
                 "I399903","I399904","I930649","I930660",
                 "I930661","IH00160","Weight","O1E1","O1E2","O1E3","O1O2","DTM","DBM","Marketvalue",
                 "HD","LD","TR","OperatingProfit","TotalAssets","OperatingRevenue","Ebit","TotalIncome","NetProfit","TotalEquity",
                 "CashEquivalent","RND","MarketCap","TotalExpense","TotalShares","CurrentAssets","CurrentLiabilities",
                 "AccumulatedDepreciation","FcffTtm","TotalLiabilities","PayrollPayable","CashPaidForEmployee","Turnover","CashFlowFromOperatingActivities",
                 "MF","FixedAssetTurnOver","VR","CirculationShares","PVcorr","PVbetacorr","COPA","CORA","COARA","VWAR","CVARR","CORRA","CashPaidForAsset","EP",
                 "BP","BETA","SMARTVWAP","REVISEDSV","LNSV","TailAmRatio","TailAR1820","TaxPayable","IncomeTax","Y3yield","ShortTermLoans","LongTermLoans",
                 "CashFlowFromFinancingActivities","CashFlowFromInvestingActivities","PE","PB","PCF","PS","DividendYield","SalesTax",
                 "DividendPayable","GrossProfit","Inventory","Listeddays","QuickRatio","CurrentRatio","TFalpha1","TFalpha2","TFalpha4","TFalpha5","TFalpha6","TFalpha7","TFalpha8","TFalpha9","TFalphaTen","TFalphaELV",
        "RVar","RSkew","RKurt","DownRvar","TStren","OpeN30","CLOSE30","HIGH30","LOW30","AMT30","VOL30","OCVP","BCVP","ILLIQ","OneTCV","OneNCV","OnePCV","FiveTCV","FiveNCV","FivePCV","VWAP30"
                ]

"""基本元"""
basic_factors = ["Open","High","Low","Close", "PreClose",
                 "AdjOpen","AdjHigh","AdjLow","AdjClose","AdjPreClose",
                 "Volume","Vwap","Amount","Avg","HaltStatus","StStatus",
                 "AdjPb","AdjReason","MarketValue","CirculationMarketValue","DealAmount",
                 "IcBenchmarkClose","IcBenchmarkOpen","IfBenchmarkOpen", "IfBenchmarkClose",
                 "IhBenchmarkClose","IhBenchmarkOpen",
                 "TurnoverRate","TurnoverValue","TurnoverVolume",
                 "I000010","I000016","I000019","I000021",
                 "I000160","I000300","I000905","I000906",
                 "I399903","I399904","I930649","I930660",
                 "I930661","IH00160","Ih50Weight","Csi300Weight","Ic500Weight",
                 "O1E1","O1E2","O1E3","O1O2","DTM","DBM","Marketvalue","HD","LD","TR","OperatingProfit","TotalAssets",
                 "OperatingRevenue","Ebit","TotalIncome","NetProfit","TotalEquity","CashEquivalent","RND","MarketCap","TotalExpense",
                 "TotalShares","CurrentAssets","CurrentLiabilities","IncomeTax"
                 "AccumulatedDepreciation","FcffTtm","TotalLiabilities","PayrollPayable","CashPaidForEmployee","Turnover","CashFlowFromOperatingActivities",
                 "MF","FixedAssetTurnOver","VR","CirculationShares","PVcorr","PVbetacorr","COPA","CORA","COARA","VWAR","CVARR","CORRA","CashPaidForAsset","EP","BP",
                 "BETA","SMARTVWAP","REVISEDSV","LNSV","TailAmRatio","TailAR1820","TaxPayable","IncomeTax","Y3yield","ShortTermLoans","LongTermLoans",
                 "CashFlowFromFinancingActivities","CashFlowFromInvestingActivities","PCF","PS","DividendYield","PE","PB","SalesTax",
                 "DividendPayable","GrossProfit","Inventory","Listeddays","QuickRatio","CurrentRatio","TFalpha1","TFalpha2","TFalpha4","TFalpha5","TFalpha6","TFalpha7","TFalpha8","TFalpha9","TFalphaTen","TFalphaELV",
        "RVar","RSkew","RKurt","DownRvar","TStren","OpeN30","CLOSE30","HIGH30","LOW30","AMT30","VOL30","OCVP","BCVP","ILLIQ","OneTCV","OneNCV","OnePCV","FiveTCV","FiveNCV","FivePCV","VWAP30"
                 ]

def I000010():
    return "I000010()"

def I000016():
    return "I000016()"

def I000019():
    return "I000019()"

def I000021():
    return "I000021()"

def I000160():
    return "I000160()"

def I000300():
    return "I000300()"

def I000905():
    return "I000905()"

def I000906():
    return "I000906()"

def I399903():
    return "I399903()"

def I399904():
    return "I399904()"

def I930649():
    return "I930649()"

def I930660():
    return "I930660()"

def I930661():
    return "I930661()"

def IH00160():
    return "IH00160()"

def Open():
    return "Open()"

def High():
    return "High()"

def Low():
    return "Low()"

def Close():
    return "Close()"

def Volume():
    return "Volume()"

def Vwap():
    return "Vwap()"

def Amount():
    return "Amount()"

def AdjOpen():
    return "AdjOpen()"

def AdjHigh():
    return "AdjHigh()"

def AdjLow():
    return "AdjLow()"

def AdjClose():
    return "AdjClose()"

def AdjPreClose():
    return "AdjPreClose()"

def AdjVolume():
    return "AdjVolume()"

def Avg():
    return "Avg()"

def HaltStatus():
    return "HaltStatus()"

def StStatus():
    return "StStatus()"

def AdjPb():
    return "AdjPb()"

def AdjReason():
    return "AdjReason()"

def MarketValue():
    return "MarketValue()"

def CirculationMarketValue():
    return "CirculationMarketValue()"

def DealAmount():
    return "DealAmount()"

def IcBenchmarkOpen():
    return "IcBenchmarkOpen()"

def IcBenchmarkClose():
    return "IcBenchmarkClose()"

def IfBenchmarkOpen():
    return "IfBenchmarkOpen()"

def IfBenchmarkClose():
    return "IfBenchmarkClose()"

def IhBenchmarkOpen():
    return "IhBenchmarkOpen()"

def IhBenchmarkClose():
    return "IhBenchmarkClose()"

def TurnoverRate():
    return "TurnoverRate()"

def TurnoverValue():
    return "TurnoverValue()"

def TurnoverVolume():
    return "TurnoverVolume()"

def Ih50Weight():
    return "Ih50Weight()"

def Csi300Weight():
    return "Csi300Weight()"

def Ic500Weight():
    return "Ic500Weight()"

def O1E1():
    return "O1E1()"

def O1E2():
    return "O1E2()"

def O1E3():
    return "O1E3()"

def OQO2():
    return "O1O2()"

def DTM():
    return "DTM()"

def DBM():
    return "DBM()"

def Marketvalue():
    return "Marketvalue()"

def HD():
    return "HD()"

def LD():
    return "LD()"

def TR():
    return "TR()"

def OperatingProfit():
    return "OperatingProfit()"

def TotalAssets():
    return "TotalAssets()"

def TotalEquity():
    return "TotalEquity()"

def OperatingRevenue():
    return "OperatingRevenue()"

def Ebit():
    return "Ebit()"

def NetProfit():
    return "NetProfit()"

def TotalIncome():
    return "TotalIncome()"

def CashEquivalent():
    return "CashEquivalent()"

def RND():
    return "RND()"

def MarketCap():
    return"MarketCap()"

def TotalExpense():
    return "TotalExpense()"

def TotalShares():
    return "TotalShares()"

def CurrentAssets():
    return "CurrentAssets()"

def CurrentLiabilities():
    return "CurrentLiabilities()"

def AccumulatedDepreciation():
    return "AccumulatedDepreciation()"

def FcffTtm():
    return "FcffTtm()"

def TotalLiabilities():
    return "TotalLiabilities()"

def PayrollPayable():
    return "PayrollPayable()"

def CashPaidForEmployee():
    return "CashPaidForEmployee()"

def Turnover():
    return "Turnover()"

def CashFlowFromOperatingActivities():
    return "CashFlowFromOperatingActivities()"

def MF():
    return "MF()"

def FixedAssetTurnOver():
    return "FixedAssetTurnOver()"

def VR():
    return "VR()"

def CirculationShares():
    return "CirculationShares()"

def PVcorr():
    return "PVcorr()"

def PVbetacorr():
    return "PVbetacorr()"

def COPA():
    return "COPA()"

def CORA():
    return "CORA()"

def COARA():
    return "COARA()"

def VWAR():
    return "VWAR()"

def CVARR():
    return "CVARR()"

def CORRA():
    return "CORRA()"

def CashPaidForAsset():
    return "CashPaidForAsset()"

def EP():
    return "EP()"

def BP():
    return "BP()"

def BETA():
    return "BETA()"

def SMARTVWAP():
    return "SMARTVWAP()"

def REVISEDSV():
    return "REVISEDSV()"

def LNSV():
    return "LNSV()"

def TailAmRatio():
    return "TailAmRatio()"

def TailAR1820():
    return "TailAR1820()"

def TaxPayable():
    return "TaxPayable()"

def IncomeTax():
    return "IncomeTax()"

def Y3yield():
    return "Y3yield()"

def ShortTermLoans():
    return "ShortTermLoans()"

def LongTermLoans():
    return "LongTermLoans()"

def CashFlowFromFinancingActivities():
    return "CashFlowFromFinancingActivities()"

def CashFlowFromInvestingActivities():
    return "CashFlowFromInvestingActivities()"

def PCF():
    return "PCF()"

def PS():
    return "PS()"

def DividendYield():
    return "DividendYield()"

def PE():
    return "PE()"

def PB():
    return "PB()"

def SalesTax():
    return "SalesTax()"

def DividendPayable():
    return "DividendPayable()"

def GrossProfit():
    return "GrossProfit()"

def Inventory():
    return "Inventory()"

def Listeddays():
    return "Listeddays()"

def QuickRatio():
    return "QuickRatio()"

def CurrentRatio():
    return "CurrentRatio()"

def OpeN30():
    return "OpeN30()"
def CLOSE30():
    return "CLOSE30()"
def HIGH30():
    return "HIGH30()"
def LOW30():
    return "LOW30()"
def AMT30():
    return "AMT30()"
def VOL30():
    return "VOL30()"
def TFalpha1():
    return "TFalpha1()"

def TFalpha2():
    return "TFalpha2()"

def TFalpha4():
    return "TFalpha4()"

def TFalpha5():
    return "TFalpha5()"

def TFalpha6():
    return "TFalpha6()"

def TFalpha7():
    return "TFalpha7()"

def TFalpha8():
    return "TFalpha8()"

def TFalpha9():
    return "TFalpha9()"

def TFalphaTen():
    return "TFalphaTen()"

def TFalphaELV():
    return "TFalphaELV()"

def TStren():
    return "TStren()"

def UpRvar():
    return "UpRvar()"

def DownRvar():
    return "DownRvar()"

def Volnew():
    return "Volnew()"

def Retnew():
    return "Retnew()"

def CVcorr():
    return "CVcorr()"

def RKurt():
    return "RKurt()"

def RSkew():
    return "RSkew()"

def RVar():
    return "RVar()"

def OCVP():
    return "OCVP()"

def BCVP():
    return "BCVP()"

def ILLIQ():
    return "ILLIQ()"

def OneTCV():
    return "OneTCV()"

def OnePCV():
    return "OnePCV()"

def OneNCV():
    return "OneNCV()"

def FiveTCV():
    return "FiveTCV()"

def FivePCV():
    return "FivePCV()"

def FiveNCV():
    return "FiveNCV()"

def VWAP30():
    return "VWAP30()"