from nltk.tokenize import word_tokenize
import nltk
from tqdm import tqdm
  

  
nltk.download('punkt')

def readFile(file_path):
    ''' read txt file line by line return a list
    file_path : str, path object or file-like object
    '''

    with open(file_path, mode ='r', encoding = 'utf8') as f:
        return f.readlines()

def tokenizer2(target_file_path, source_file_path, caseSensetive = True, singleLine = True, language = 'english'):
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
    
    for i in tqdm (range(len(text)), desc="progressing..."):
        with open(target_file_path,'a',encoding = 'utf8') as f:
            
            if caseSensetive:
                if singleLine:
                    tokens = ' '.join(word_tokenize(text[i], language=language, preserve_line=False))
                else:
                    data = ' '.join(word_tokenize(text[i], language=language, preserve_line=False)) 
                    tokens = data + '\n'
            else:
                if singleLine:
                    tokens = ' '.join(word_tokenize(text[i], language='english', preserve_line=False)).lower()
                else:
                    data = ' '.join(word_tokenize(text[i], language=language, preserve_line=False)) 
                    tokens = data + '\n'
            
            f.write(tokens+' ')
