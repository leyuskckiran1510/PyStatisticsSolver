import requests
import re
import os
import dotenv
import compressor
import color 

dotenv.load_dotenv()


class Statistics:
    def __init__(self, data,typ):
        self.typ = typ
        self.raw_data = data
        self.data = data
        self._clean()
        self.balanced_data = self.balance_continious_data()
        self._midandother()
        self.N = sum([i[1] for i in self.data])
        self.x = [i[0] for i in self.data]
        self.f = [i[len(self.balanced_data[0])-1] for i in self.balanced_data] if len(self.balanced_data[0])!=1 else [i[1] for i in self.data]
        self.fx = [self.f[i]*self.x[i] for i in range(len(self.f))]
        self.midx = [(self.balanced_data[i][1]+self.balanced_data[i][0])/2   for i in range(len(self.f))] if len(self.balanced_data[0])==3  else [self.data[i][0] for i in range(len(self.f))]
        self.cumulative = self._cumulative()
        self.mean = self._mean()
        self.median = self._median()
        self.mode = self._mode()
        self.range = self._range()
        self.variance = self._variance()
        self.std_dev = self._std_dev()
        self.skewness = self._skewness()
        self.kurtosis = self._kurtosis()
        self.quartiles = self._quartiles()





    def _cumulative(self):
        cum_lis=[]
        for n,i in enumerate(self.data):
            cum_lis.append(i[1]+cum_lis[n-1] if n!= 0 else i[1])
        return cum_lis

        
    def _clean(self):
        value={}
        sample=[]
        for i in self.data:
            ln = len(i)
            if ln not in value.keys():
                sample.append(i)
                value[ln]=1
                continue
            value[ln]+=1
        ttl = sorted(value.values())[0]
        for n in range(0,len(self.data)):
            if len(self.data[n])>ttl:
                for _ in range(len(self.data[n])-ttl):
                    self.data[n].pop(0)
            if len(self.data[n])<ttl:
                self.data[n]+[1]




    def balance_continious_data(self):
        if(len(self.data[0])!=3):
            return self.data
        offset = (self.data[1][0]-self.data[0][1])/2
        return [[i[0]-offset,i[1]+offset,i[2]] if i[0]!=0 else [i[0],i[1]+offset,i[2]] for i in self.data]     
        
        

    def _midandother(self):
        temp=[]
        for i in self.data:
            if len(i)==3:
                temp.append([(i[0]+i[1])/2,i[2]])
            elif len(i)==2:
                temp.append([i[0],i[1]])
            elif len(i)==1:
                if i[0] not in temp:
                    temp.append([i[0],self.data.count([i[0]])])
            else:
                temp.append([0,0])
        self.data = temp


    def _mean(self):
        return sum(list(map(lambda x:x[0]*x[1],self.data)))/self.N

    def stat_print(self):
        print("Statistics:")
        val=75
        print(f"{color.Back.RGB(val,val,val)}\033[2J")
        print(f"{color.Fore.RGB(255,0,0)}raw_X   \t{color.Fore.RGB(0,200,0)}X           \t{color.Fore.RGB(0,0,200)}mid-x\t{color.Fore.RGB(200,200,0)}f\t{color.Fore.RGB(200,200,200)}cf\t{color.Fore.RGB(0,200,200)}fx")
        for i in range(len(self.data)):
            print(f"{color.Fore.RGB(255,0,0)}{self.raw_data[i][:-1]}\t{color.Fore.RGB(0,200,0)}{self.balanced_data[i][:-1]}\t{color.Fore.RGB(0,0,200)}{self.midx[i]}\t{color.Fore.RGB(200,200,0)}{self.f[i]}\t{color.Fore.RGB(200,200,200)}{self.cumulative[i]}\t{color.Fore.RGB(0,200,200)}{self.fx[i]}")
        


    def _median(self):
        diff_dic={}
        for n,i in enumerate(self.cumulative):
                if i>self.N/2:
                    diff_dic[abs(i-(self.N/2))] = n
        a=sorted(diff_dic.items())[0][1]
        if len(self.balanced_data[0])==3:
            median_class = self.balanced_data[a]
            return median_class[0] +abs(median_class[0]-median_class[1]) * ((self.N/2 - self.cumulative[a-1])/self.f[a])
        elif len(self.balanced_data[0])==2:
            return self.data[a][0]
        else:
            return self.data[a][0]
        return 0

    def _mode(self):
        return self.data[self.f.index(max(self.f))][0]
    
    def _range(self):
        return f"{self.data[-1][0]}-{self.data[0][0]}"
    
    def _variance(self):
        return sum(list(map(lambda x:(x[0]-self.mean)**2*x[1],self.data)))/self.N

    def _std_dev(self):
        return self.variance**0.5

    def _skewness(self):
        return sum(list(map(lambda x:(x[0]-self.mean)**3*x[1],self.data)))/(self.N*self.std_dev**3)

    def _kurtosis(self):
        return sum(list(map(lambda x:(x[0]-self.mean)**4*x[1],self.data)))/(self.N*self.std_dev**4)

    def _quartiles(self):
        q1 = self._quartile(0.25)
        q2 = self._quartile(0.50)
        q3 = self._quartile(0.75)
        return [q1,q2,q3]

    def _quartile(self,quartile):
        diff_dic={}
        for n,i in enumerate(self.cumulative):
                if i>self.N*quartile:
                    diff_dic[abs(i-(self.N*quartile))] = n
        a=sorted(diff_dic.items())[0][1]
        if len(self.balanced_data[0])==3:
            median_class = self.balanced_data[a]
            return median_class[0] +abs(median_class[0]-median_class[1]) * ((self.N*quartile - self.cumulative[a-1])/self.f[a])
        elif len(self.balanced_data[0])==2:
            return self.data[a][0]
        else:
            return self.data[a][0]


class Regression:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.N = len(x)
        self.x_mean = sum(x)/self.N
        self.y_mean = sum(y)/self.N
        self.x_std_dev = (sum(list(map(lambda x:(x-self.x_mean)**2,self.x)))/self.N)**0.5
        self.y_std_dev = (sum(list(map(lambda x:(x-self.y_mean)**2,self.y)))/self.N)**0.5
        self.covariance = sum(list(map(lambda x,y:(x-self.x_mean)*(y-self.y_mean),self.x,self.y)))/self.N
        self.correlation = self.covariance/(self.x_std_dev*self.y_std_dev)
        self.slope = self.covariance/sum(list(map(lambda x:(x-self.x_mean)**2,self.x)))/self.N
        self.intercept = self.y_mean - self.slope*self.x_mean
        self.predicted_y = list(map(lambda x:self.slope*x+self.intercept,self.x))
        self.error = sum(list(map(lambda x,y:(x-y)**2,self.y,self.predicted_y)))/self.N
        self.r_squared = 1-(self.error/self.y_std_dev**2)
        self.equation = f"y = {self.slope}x + {self.intercept}"

    def predict(self,x):
        return self.slope*x+self.intercept

    def print(self):
        print(f"X Mean: {self.x_mean} Y Mean: {self.y_mean}")
        print(f"X Standard Deviation: {self.x_std_dev} Y Standard Deviation: {self.y_std_dev}")
        print(f"Covariance: {self.covariance}")
        print(f"Correlation: {self.correlation}")
        print(f"Slope: {self.slope} Intercept: {self.intercept}")
        print(f"Error: {self.error}")
        print(f"R Squared: {self.r_squared}")
        print(f"Equation: {self.equation}")




def extract(name='a.jpg'):
    compressed=False
    if os.path.getsize(name)>1024**2:
        print("[*]Image To Large Compressing...")
        name = compressor.compress_img(name,bw=True)
        compressed =True
    print("[*]Generating Text From Image")
    url = 'https://api.ocr.space/parse/image'
    api = os.getenv("API_KEY") if os.getenv("API_KEY") else 'donotstealthiskey8589'
    with open(name, 'rb') as image_file:
        payload = {
            'apikey':api,
            'language': 'eng',
            'FileType': '.Auto',
            'isTable': 'true',
            'scale': 'true',
            'OCREngine': '2',
            }
        response = requests.post(url,files={name:image_file},data=payload)
        try:
            os.remove(name) if compressed else ''
            return response.json()['ParsedResults'][0]['ParsedText']
        except KeyError as e:
            print("KeyError:- Avilable Keys are",response.json().keys())
        except Exception as e:
            print("Other Exceptin Occured ie:-",e,response.text)

    if compressed:
        print("[-]Removing Compressed Image")
        os.remove(name) 
    else:
        pass

def flatten_list(nested_list, flattened_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten_list(item, flattened_list)
        else:
            flattened_list.extend([int(item)])


def parser(string,typ=0):
    pattren=[r"\d{1,9}[-|\s]\d{0,9}\s+\d+", r"\d{1,9}"]
    final=[]
    string = string.replace("\t","    ").replace("\n","    ").replace("\r",'    ')
    matches = re.findall(pattren[typ],string)
    for match in matches:
        blnk=[]
        lis = [i.split("-") for i in match.split(" ")]
        lis = [i for i in lis if i!=['']]
        flatten_list(lis,blnk) 
        final.extend([blnk])
    return final,typ



def test():
    vert='''3. Check the following requency distribUion talble, co1S
Weights (in kg) Number of stud
31 35   9
36 40   5
41-45   14
46-50   3
51-55   1
56 60   2
61 65   2
66 70   1
71 75   1
() What is class-interval for classes 31 35?
() How many students are there in the range of 41-45 kgs?
Salu

    '''
    hori='''Number of wickets
Number of bowlers
20-60
7
60-100
5
100-150
16
150-250
12
250-350
2
350-450
3
'''
    dis='''>140
4
>145
11
>150
29
>155
40
>160
46
>165
51
'''
    indv="25 36 42 55 60 62 73 75 78 95"
    #c= parser(extract("image.jpg"))
    #c=parser("'Height (in cm)\tNumber of girls\t\r\n1 140\t4\t\r\n145\t11\t\r\n150\t29\t\r\n>1 155\t\r\n1 160\t\r\n165\t51\t\r\n'",0)
    c= parser(hori)
    #c= parser(indv,1)
    print(c)
    d= Statistics(c)
    # pprint(d.raw_data)
    # pprint(d.data)
    # pprint(d.balanced_data)
    # pprint(d.cumulative)
    d.stat_print()
    print("Mean:-",d.mean)
    print("Median:-",d.median)
    print("Mode:-",d.mode)
    print("Range:-",d.range)
    print("Variance:-",d.variance)
    print("Standard Deviation:-",d.std_dev)
    print("Quartile:-",d.quartiles)
    print("Skewness:-",d.skewness)
    print("Kurtosis:-",d.kurtosis)
    print("\n"*5)
    

    
    




def main():
    test()



if __name__=="__main__":
    main()