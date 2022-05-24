from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def readFile(file_path):
    ''' read txt file line by line return a list
    file_path : str, path object or file-like object
    '''

    with open(file_path, mode ='r', encoding = 'utf8') as f:
        return f.readlines()

def tokenizer(target_file_path, source_file_path, caseSensetive = True):
    """
    tokenizer use word_tokenize from nltk library. Only accept txt file for tokenizing.

    target_file_path : str, path object or file-like object
    Any valid string path is acceptable. create a new file defined path

    source_file_path: str, path object or file-like object
    Any valid string path is acceptable.

    caseSensetive : bool, default True. for text case or uncased


    """
    

    with open(source_file_path, mode ='r', encoding = 'utf8') as f:
        text = f.readlines()
    
    for i in text[:3]:
        with open(target_file_path+'.txt','a',encoding = 'utf8') as f:
            
            if caseSensetive:
                tokens = ' '.join(word_tokenize(i, language='english', preserve_line=False))
            else:
                tokens = ' '.join(word_tokenize(i, language='english', preserve_line=False)).lower()
            
            f.write(tokens+' ')        
