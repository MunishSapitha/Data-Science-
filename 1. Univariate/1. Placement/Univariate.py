class Univariate():
    
    #QualQuan Function   
    def qualQuan(dataset):   
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            # print(columnName)
            if (dataset[columnName].dtypes=='O'):
                # print("Qual")
                qual.append(columnName)
            else:
                # print("Quan") 
                quan.append(columnName)
        return qual,quan   


    
    # MeanMedianMode Function   
    def MeanMedianMode():
        descriptive=pd.DataFrame(index=["Mean","Median","Mode"],columns=quan)
        
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            
        return descriptive
    
    
    
    # Percentile Function
    def Percentile():
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:99%","Q4:100%"],columns=quan)
            
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:99%"]=np.percentile(dataset[columnName],99)   # np.percentile
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]  # as described in dataset.describe for 100%
        return descriptive 
    
    
    
    # IQR,Outlier Function
    def IQROutlier():
        descriptive=pd.DataFrame(index=["Mean", "Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","LesserOutlier","GreaterOutlier","min values","max values"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]

            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)   # np.percentile
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]  # as described in dataset.describe for 100%

            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["LesserOutlier"]=descriptive[columnName]["Q1:25%"]- descriptive[columnName]["1.5rule"]
            descriptive[columnName]["GreaterOutlier"]=descriptive[columnName]["Q3:75%"]+ descriptive[columnName]["1.5rule"]
            descriptive[columnName]["min values"]=dataset[columnName].min()
            descriptive[columnName]["max values"]=dataset[columnName].max()

        return descriptive  

    
    
    # Potential Outlier Function
    def PotentialOutlier(lesser,greater):
        lesser=[]
        greater=[]

        for columnName in quan:
            if descriptive[columnName]["min values"]< descriptive[columnName]["LesserOutlier"]:
                lesser.append(columnName)

            if descriptive[columnName]["max values"]> descriptive[columnName]["GreaterOutlier"]:
                greater.append(columnName)

        return lesser,greater
    
    
    
    #Replace Potential Outlier Function
    def ReplacePO(lesser,greater):
        for columnName in lesser:
             dataset[columnName][dataset[columnName]<descriptive[columnName]["LesserOutlier"]]=descriptive[columnName]["LesserOutlier"]

        for columnName in greater:
             dataset[columnName][dataset[columnName]>descriptive[columnName]["GreaterOutlier"]]=descriptive[columnName]["GreaterOutlier"]

        return lesser,greater
    
    
    
    #Frequency, Relative F, Cumulative RF Function  
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique values","Frequency","Relative Frequency","Cumulative RF"])

        freqTable["Unique values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=freqTable["Frequency"]/103
        freqTable["Cumulative RF"]=freqTable["Relative Frequency"].cumsum()
        
        return freqTable

    
    
    # Skewness and Kurtosis Function

    def SkewKurtosis():
        descriptive=pd.DataFrame(index=["Mean", "Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","LesserOutlier","GreaterOutlier","min values","max values","Skewness","Kurtosis"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]

            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)   # np.percentile
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]  # as described in dataset.describe for 100%

            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["LesserOutlier"]=descriptive[columnName]["Q1:25%"]- descriptive[columnName]["1.5rule"]
            descriptive[columnName]["GreaterOutlier"]=descriptive[columnName]["Q3:75%"]+ descriptive[columnName]["1.5rule"]
            descriptive[columnName]["min values"]=dataset[columnName].min()
            descriptive[columnName]["max values"]=dataset[columnName].max()

            descriptive[columnName]["Skewness"]=dataset[columnName].skew()
            descriptive[columnName]["Kurtosis"]=dataset[columnName].kurtosis()


        return descriptive  