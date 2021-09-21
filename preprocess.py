import pandas as pd
import glob
import os

mypath = r'C:\Users\PCR\Desktop\Spectra\Batch 2\2 - Days'
finalpath = [ f.path for f in os.scandir(mypath) if f.is_dir() ]

for path in finalpath:
    all_files = glob.glob(path + "/*.xls")
    
    finaldf = pd.DataFrame()
    
    for file in all_files:
        newdf = pd.DataFrame()
        spectra = pd.DataFrame()
        bgs = pd.DataFrame()
        df = pd.read_excel(file)
    
        columns = list(df)
        columns.remove("White")
        columns.remove("Wavelength [nm]")
        for i in columns:
            df[i] = df[i]/df["White"]
        df = df.drop("White", axis = 1)
        
        wv = df["Wavelength [nm]"]
        df = df.drop(df.index[0:19])
        df = df.drop(df.index[135:185])
        df = df.drop("Wavelength [nm]", axis = 1)
    
        for i in range(0, int(len(df.columns)/2)):
            newdf[i] = df.iloc[:,i]/df.iloc[:,int((len(df.columns)/2)+i)]
        
        newdf = newdf.T
        finaldf = pd.concat([finaldf, newdf], ignore_index = True)
    
    finaldf = finaldf.T
    finaldf = (finaldf - finaldf.mean()) / finaldf.std()
    finaldf = finaldf.T
    finaldf.rename(columns = wv, inplace = True)
    finaldf["age"] = int(os.path.basename(path))
    csvname = "\\" + os.path.basename(path) + ".csv"
    print(finaldf)
    finaldf.to_csv(os.path.dirname(path) + csvname)
