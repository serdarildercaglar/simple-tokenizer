from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def readFile(file_path):
    with open(file_path, mode ='r', encoding = 'utf8') as f:
        return f.readlines()

def tokenizer(target_file_path, source_file_path, caseSensetive = True):
    import nltk
    nltk.download('punkt')

    with open(source_file_path, mode ='r', encoding = 'utf8') as f:
        text = f.readlines()
    
    for i in text[:3]:
        with open(target_file_path+'.txt','a',encoding = 'utf8') as f:
            
            if caseSensetive:
                tokens = ' '.join(word_tokenize(i, language='english', preserve_line=False))
            else:
                tokens = ' '.join(word_tokenize(i, language='english', preserve_line=False)).lower()
            
            f.write(tokens+' ')        