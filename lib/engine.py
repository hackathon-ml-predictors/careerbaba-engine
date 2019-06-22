import pandas as pd
import numpy as np
from sklearn import decomposition
import matplotlib.pyplot as plt
import pickle

def train(dataset):
    data = dataset.iloc[:,:-1].values
    label = dataset.iloc[:,-1].values

    print (len(data[0]))

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder

    labelencoder = LabelEncoder()

    for i in range(14,38):
        data[:,i] = labelencoder.fit_transform(data[:,i])
    
    print(data[:5])

    print(data[:5,14:])

    from sklearn.preprocessing import Normalizer

    data1=data[:,:14]

    normalized_data = Normalizer().fit_transform(data1)

    print(normalized_data.shape)

    data2=data[:,14:]

    data2.shape

    df1 = np.append(normalized_data,data2,axis=1)

    df1.shape

   #  X1 = pd.DataFrame(df1,columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
   #     'Percentage in Programming Concepts',
   #     'Percentage in Software Engineering', 'Percentage in Computer Networks',
   #     'Percentage in Electronics Subjects',
   #     'Percentage in Computer Architecture', 'Percentage in Mathematics',
   #     'Percentage in Communication skills', 'Hours working per day',
   #     'Logical quotient rating', 'hackathons', 'coding skills rating',
   #     'public speaking points', 'can work long time before system?',
   #     'self-learning capability?', 'Extra-courses did', 'certifications',
   #     'workshops', 'talenttests taken?', 'olympiads',
   #     'reading and writing skills', 'memory capability score',
   #     'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
   #     'Type of company want to settle in?',
   #     'Taken inputs from seniors or elders', 'interested in games',
   #     'Interested Type of Books', 'Salary Range Expected',
   #     'In a Realtionship?', 'Gentle or Tuff behaviour?',
   #     'Management or Technical', 'Salary/work', 'hard/smart worker',
   #     'worked in teams ever?', 'Introvert'])
    

    X1 = pd.DataFrame(data,columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
       'Percentage in Programming Concepts',
       'Percentage in Software Engineering', 'Percentage in Computer Networks',
       'Percentage in Electronics Subjects',
       'Percentage in Computer Architecture', 'Percentage in Mathematics',
       'Percentage in Communication skills', 'Hours working per day',
       'Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'can work long time before system?',
       'self-learning capability?', 'Extra-courses did', 'certifications',
       'workshops', 'talenttests taken?', 'olympiads',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'interested in games',
       'Interested Type of Books', 'Salary Range Expected',
       'In a Realtionship?', 'Gentle or Tuff behaviour?',
       'Management or Technical', 'Salary/work', 'hard/smart worker',
       'worked in teams ever?', 'Introvert'])   
    X1.head()

    print('actual data')
    print(X1.head(1))  

    le = LabelEncoder()
    label_in_string = label

    le.fit(list(label))
    #  label = labelencoder.fit_transform(label)
    le.transform(list(label))
    print(len(label))

    y=pd.DataFrame(label,columns=["Suggested Job Role"])
    y.head()

    from sklearn import tree
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing 
    from sklearn.metrics import accuracy_score

    X_train,X_test,y_train,y_test=train_test_split(X1,y,test_size=0.2,random_state=10) 

    clf = tree.DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
    clf = clf.fit(X_train, y_train)

    from sklearn.metrics import confusion_matrix,accuracy_score

    y_pred = clf.predict(X_test)

    cm = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    
    
    y_pred_num = y_pred
   #  y_pred = le.inverse_transform(y_pred)
    y_pred = pd.DataFrame(y_pred)
    
    print(y_pred.head())

    print("confusion matrics=",cm)
    print("  ")
    print("accuracy=",accuracy*100)
    #pickle list object

    numbers_list = [1, 2, 3, 4, 5]
    list_pickle_path = 'list_pickle.pkl'

    

    # Create an variable to pickle and open it in write mode
    #  list_pickle = open(list_pickle_path, 'wb')
    #  pickle.dump(clf, list_pickle)
    #  list_pickle.close()

    with open(list_pickle_path, 'wb') as f:
      pickle.dump(clf, f)

    """
    test pickled function
    """ 
    print("pickled output")
    saved_model = pickle.dumps(clf) 
  
    # Load the pickled model 
    knn_from_pickle = pickle.loads(saved_model) 
   
    # Use the loaded pickled model to make predictions 
    y_pred_test = knn_from_pickle.predict(X_test) 
    print(y_pred_test)

def get_recommanded_job(jsonPostData):
    list_pickle_path = 'list_pickle.pkl'
    with open(list_pickle_path, 'rb') as f:
      clf = pickle.load(f)

    


    # Loading the saved decision tree model pickle
    #decision_tree_pkl_filename = 'list_pickle.pkl'
    #decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
    #decision_tree_model = pickle.load(decision_tree_model_pkl)
    
    #y_pred = decision_tree_model.predict(jsonPostData)
    y_pred = clf.predict(jsonPostData)
    print(y_pred)
    return y_pred  
    




    

