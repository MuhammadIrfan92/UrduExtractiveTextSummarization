from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import re
import string
import unicodedata

def get_stop_words(path='stopwords.txt'):
    with open(path, 'r') as file:
        data = file.read()

    words = data.split(":")
    return words


def read_raw_file(path = "text.txt"):
    with open(path, 'r') as file:
        data = file.read()
    data = data.replace("\n","۔")
    data = data.split("۔")
    print(len(data))
    return data


def write_file(data, path='temp.txt'):
    with open(path, 'w') as file:
        for i in data:
            file.write(f"{i}\n")
            
            
def remove_stopwords(text_list, stop_words):
    filtered_data = []
    for i in text_list:
        if i not in stop_words:
            filtered_data.append(i)
    return " ".join(filtered_data)  

# def process(path = 'text.txt', stop_words = get_stop_words()):
#     with open(path, 'r', encoding='utf-8') as file:
#         data = file.read()
    
#     # create list having each sentence as element
#     data = data.replace("\n", "۔")
#     data = data.split("۔")
#     # print(data)
#     # print(len(data))
    
#     # remove punctuations from sentences
    
#     for i in range(len(data)):
#         if data[i] != '':
#             data[i] = ''.join(c for c in data[i] if unicodedata.category(c) != 'Po')
    
#     # Remove stopwords
#     for i in range(len(data)):
#         data[i] = remove_stopwords(data[i].split(" "), stop_words)
        
#     return data



def process(raw_text, stop_words):
    
    # create list having each sentence as element
    data = raw_text.replace("\n", "۔")
    data = data.split("۔")
    # print(data)
    # print(len(data))
    
    # remove punctuations from sentences
    
    for i in range(len(data)):
        if data[i] != '':
            data[i] = ''.join(c for c in data[i] if unicodedata.category(c) != 'Po')
    
    # Remove stopwords
    for i in range(len(data)):
        data[i] = remove_stopwords(data[i].split(" "), stop_words)
        
    return data
             
        


def word_freq_cal(text_list):
    fdist = {}
    
    for sent in text_list:
        for word in sent.split(" "):
            if word not in fdist:
                fdist[word] = 1
            else:
                fdist[word] += 1
    
    return fdist



    
def assign_word_freq(text_list, word_freq):
    result_temp = []
    sent_no = 0
    for i in text_list:
        sent_dict = {}
        score = 0
        for j in i.split(" "):
            if j not in sent_dict: # only unique words, is best strategy
                sent_dict[j] = word_freq[j]
                score += word_freq[j]
        result_temp.append([sent_no, score, sent_dict])
        sent_no += 1
        
    return result_temp
        
# text_list = process()
# word_freq = word_freq_cal(text_list)

# print(len(word_freq))
# res = assign_word_freq(text_list, word_freq)

# sorted_list = sorted(res, key=lambda x: x[1])

# for i in sorted_list:
#     print(i)
    
# output_sent = 1  
# result = read_raw_file()

# index = sorted_list[-1][0]

# print(result[index])
# with open('result.txt', 'w') as file:
#     file.write(f"{result[index]}")
    
def ExtractiveTextSummarization(raw_text, n_sentences):
    stop_words = ['انھوں', 'جائے', 'کو', 'کیا', 'کیوں', 'کون', 'کس', 'کسے', 'کن', 'کنہیں', 'کونسی', 'کونسے', 'کونسا', 'کوئی', 'کچھ', 'کسی', 'بعض', 
                  'بعضے', 'فلاں', 'کل', 'چند', 'سب', 'ہر', 'سبھی', 'جیسا', 'جیسی', 'جیسے', 'وہ', 'جیسوں', 'میرا', 'میری', 'میرے', 'میروں', 'مرا', 'مری', 'مرے',
                  'تمہارا', 'تمہاری', 'تمہارے', 'تمہاروں', 'تیرا', 'ترا', 'تری', 'ترے', 'تیری', 'تیرے', 'تیروں', 'ہمارا', 'ہماری', 'ہمارے', 'ہماروں', 'اسکا', 
                  'اسکی', 'اسکے', 'انکا', 'انکی', 'مجھ', 'مجھے', 'مجھی', 'آپ', 'تم', 'تمہیں', 'تجھ', 'تجھے', 'تجھی', 'ہم', 'ہمیں', 'ہمی', 'اس', 'اسے', 'انہیں',
                  'انہوں', 'کب', 'کہاں', 'کدھر', 'یہ', 'وہ', 'جنہوں', 'جدھر', 'جہاں', 'جو', 'جس', 'جسے', 'جن', 'جنہیں', 'انکے', 'خود', 'اپنےآپ', 'اپنی', 
                  'اپنے', 'اپنا', 'اپنوں', 'ان', 'یہی', 'وہی', 'اسی', 'انہی', 'ایسا', 'ویسا', 'کیسا', 'چنانچہ', 'حالانکہ', 'تاکہ', 'بشرطیکہ', 'اس لیے', 'ہرچند', 
                  'پس', 'نیز', 'پر', 'خواه', 'اگر', 'وگرنہ', 'کیونکر', 'ولے', 'تب', 'کیونکہ', 'گو', 'تاہم', 'لیکن', 'یا', 'ورنہ', 'اور', 'البتہ', 'تو', 'سو', 'و',
                  'مگر', 'بلکہ', 'اگرچہ', 'چونکہ', 'کہ', 'لہذا', 'پہ', 'سے', 'نے', 'کو', 'کا', 'کی', 'کے', 'گا', 'گی', 'گے', 'تھا', 'تھے', 'تھی', 'تھیں', 'ہے', 
                  'ہیں', 'ہو', 'ہوں', 'خاطر', 'سمیت', 'فقط', 'محض', 'فی', 'از', 'دریں', 'قبل', 'واسطے', 'تک', 'تلک', 'میں', 'تا', 'با', 'علاوه', 'بجز', 'ماسوا', 
                  'بنا', 'جز', 'بغیر', 'سوائے', 'الا', 'قطعا', 'مطلق', 'ہرگز', 'سراسر', 'صرف', 'ضرور', 'بالکل', 'بالضرور', 'بےشک', 'جی', 'ہاں', 'نہیں', 'نا', 'مت', 
                  'لا', 'بے', 'نہ', 'مانند', 'مثل', 'ہوبہو', 'گویا', 'نما', 'طرح', 'سا', 'سی', 'ایسے', 'سہی', 'بھی', 'ہی', 'تھو', 'اخاه', 'اہاہا', 'ہائیں', 'ہائے', 
                  'آہا', 'چھی', 'افوه', 'اف', 'آه', 'اوہو', 'واه', 'اب', 'یعنی', 'ری', 'اوئے', 'ابے', 'ارے', 'اری', 'رے', 'او', 'اجی', 'اے', 'نے', 'اس', 'آ', 'نے', 
                  'اس', 'آ', 'میں', 'پبئے', 'ہوبری', 'طرف', 'ثہت', 'گئے', 'اپٌے', 'گی', 'خو', 'اثھی', 'پر', 'ہر', 'ضے', 'ثھی', 'گب', 'کت', 'گیب', 'دوضری',
                  'اپٌب', 'تھی', 'وٍ', 'ضکتے', 'ثعذ', 'ہے', 'لگیں', 'گے', 'دی', 'اش', 'تھب', 'ًے', 'ضکتی', 'ثدبئے', 'یہ', 'والے', 'لئے', 'دیب', 'اى', 'تو', 'ًہیں', 
                  'ضکتب', 'ثبہر', 'ہوًے', 'ہوبرا', 'لگی', 'رریعے', 'اًذر', 'کیب', 'توبم', 'ہوبرے', 'کب', 'ہوں', 'ہوضکتب', 'لگے', 'رہب', 'اور', 'کی', 'تک', 'ہو', 'کریں',
                  'ہیں', 'ہوضکتی', 'هگر', 'رہی', 'ایطے', 'ہوا', 'کہ', 'تت', 'ہوًب', 'کیطے', 'ہوضکتے', 'هیں', 'رہے', 'ایک', 'کے', 'خت', 'ًہ', 'ہوتب', 'کیوں', 'تھے', 
                  'ًب', 'ضبتھ', 'آئے', 'خب', 'ثبرے', 'رریعے', 'کوئی', 'کیطب', 'رکھ', 'خبرہے', 'ثغیر', 'پھر', 'کطی', 'رریعہ', 'خبرہب', 'ثراں', 'کیطرف', 'رکھتب', 'خجکہ',
                  'ثلکہ', 'اضطرذ', 'کررہی', 'دوضرے', 'توہیں', 'ثبئیں', 'کیلئے', 'رکھتبہوں', 'خص', 'ثٌذ', 'اضکب', 'ثرآں', 'خبرہی', 'کررہے', 'دوًوں', 'کیوًکہ', 'رکھتی',
                  'خوکہ', 'ثیچ', 'اضکی', 'یہبں', 'کررہب', 'دوراى', 'توہی', 'کےثعذ', 'رکھتے', 'خیطب', 'پچھلا', 'اضکے', 'ضکب', 'دوضروں', 'زکویہ', 'چکے', 'تھوڑا', 'پطٌذ',
                  'ثي', 'اًہیں', 'ٓ', '', 'آش', 'ضکٌب', 'دیتب', 'خبهوظ', 'چلا', 'تھوڑی', 'پل', 'ثٌب', 'اوًچب', 'اة', 'ضکی', 'دیتی', 'ختن', 'چلو', 'تھوڑے', 'پوچھب', 'ثٌبرہب',
                  'اوًچبئی', 'اخبزت', 'ضکے', 'دیتے', 'در', 'چلیں', 'تیي', 'پوچھتب', 'ثٌبرہی', 'اوًچی', 'اچھب', 'ضلطلہ', 'دیر', 'درخبت', 'چلے', 'خبًب', 'پوچھتی', 'ثٌبرہے',
                  'اوًچے', 'اچھی', 'ضوچ', 'دیکھٌب', 'درخہ', 'چھوٹب', 'خبًتب', 'پوچھتے', 'ثٌبًب', 'اٹھبًب', 'اچھے', 'ضوچب', 'دیکھو', 'درخے', 'چھوٹوں', 'خبًتی', 'پوچھٌب', 'ثٌذ',
                  'اہن', 'اختتبم', 'ضوچتب', 'دیکھی', 'درزقیقت', 'چھوٹی', 'خبًتے', 'پوچھو', 'ثٌذکرًب', 'آئی', 'ادھر', 'ضوچتی', 'دیکھیں', 'درضت', 'چھوٹے', 'خبًٌب', 'پوچھوں',
                  'ثٌذکرو', 'آئے', 'ارد', 'ضوچتے', 'دیٌب', 'دش', 'چھہ', 'خططرذ', 'پوچھیں', 'ثٌذی', 'آج', 'اردگرد', 'ضوچٌب', 'دے', 'دفعہ', 'چیسیں', 'خگہ', 'پورا', 'ثڑا',
                  'آخر', 'ارکبى', 'ضوچو', 'راضتوں', 'دکھبئیں', 'زبصل', 'خگہوں', 'پہلا', 'ثڑوں', 'آخرکبر', 'اضتعوبل', 'ضوچی', 'راضتہ', 'دکھبتب', 'زبضر', 'خگہیں',
                  'پہلی', 'ثڑی', 'آدهی', 'اضتعوبلات', 'ضوچیں', 'راضتے', 'دکھبتی', 'زبل', 'خلذی', 'پہلےضی', 'ثڑے', 'آًب', 'اغیب', 'ضیذھب', 'رکي', 'دکھبتے', 'زبل', 
                  'خٌبة', 'پہلےضے', 'ثھر', 'آٹھ', 'اطراف', 'ضیذھی', 'رکھب', 'دکھبًب', 'زبلات', 'خواى', 'پہلےضےہی', 'ثھرا', 'آیب', 'افراد', 'ضیذھے', 'رکھی', 'دکھبو', 
                  'زبلیہ', 'خوًہی', 'پیع', 'ثھراہوا', 'ثب', 'اکثر', 'ضیکٌڈ', 'رکھے', 'دکھبیب', 'زصوں', 'خیطبکہ', 'تبزٍ', 'ثھرپور', 'ثبترتیت', 'اکٹھب', 'غبیذ', 'زیبدٍ',
                  'دلچطپ', 'زصہ', 'چبر', 'تر', 'ثہتر', 'ثبری', 'اکٹھی', 'غخص', 'ضبت', 'دلچطپی', 'زصے', 'چبہب', 'ترتیت', 'ثہتری', 'ثبلا', 'اکٹھے', 'غذ', 'ضبدٍ',
                  'دلچطپیبں', 'زقبئق', 'چبہٌب', 'تریي', 'ثہتریي', 'ثبلترتیت', 'اکیلا', 'غروع', 'ضبرا', 'هٌبضت', 'زقیتیں', 'چبہے', 'تعذاد', 'پبش', 'ثرش', 'اکیلی',
                  'غروعبت', 'ضبرے', 'دو', 'زقیقت', 'چکب', 'تقریجباً', 'پبًب', 'ثغیر', 'اکیلے', 'غے', 'ضبل', 'دور', 'زکن', 'چکی', 'تن', 'پبًچ', 'ثلٌذ', 'اگرچہ', 'صبف',
                  'ضبلوں', 'دوضرا', 'زکوباً', 'چکیں', 'تٌہب', 'پراًب', 'ثلٌذوثبلا', 'الگ', 'کہتے', 'کرتی', 'طریق', 'ًیب', 'هطئلے', 'لازهی', 'کوًطے', 'قجیلہ', 'صسیر', 'کہٌب',
                  'کرتے', 'طریقوں', 'وار', 'هطبئل', 'لگتب', 'کھولا', 'قطن', 'صفر', 'کہٌب', 'کرتےہو', 'طریقہ', 'وار', 'هطتعول', 'لگتی', 'کھولٌب', 'کئی', 'صورت', 'کہو',
                  'کرًب', 'طریقے', 'ٹھیک', 'هػتول', 'لگتے', 'کھولو', 'کئے', 'صورتسبل', 'کہوں', 'کرو', 'طور', 'ڈھوًڈا', 'هطلق', 'لگٌب', 'کھولی', 'کبفی', 'صورتوں', 'کہی',
                  'کریں', 'طورپر', 'ڈھوًڈلیب', 'هعلوم', 'لگی', 'کھولیں', 'کبم', 'صورتیں', 'کہیں', 'کرے', 'ظبہر', 'ڈھوًڈًب', 'هکول', 'لگے', 'کھولے', 'کجھی', 'ضرور',
                  'کہیں', 'کل', 'عذد', 'ڈھوًڈو', 'هلا', 'لوجب', 'کہب', 'کرا', 'ضرورت', 'کہے', 'کن', 'عظین', 'ڈھوًڈی', 'هوکي', 'لوجی', 'کہتب', 'کرتب', 'ضرورتباً', 'کیے',
                  'کوتر', 'علاقوں', 'ڈھوًڈیں', 'هوکٌبت', 'لوجے', 'کہتی', 'کرتبہوں', 'ضروری', 'کےرریعے', 'کورا', 'علاقہ', 'ہورہے', 'ًبپطٌذ', 'لے', 'ہن', 'هوکٌہ', 'لوسبت',
                  'گئی', 'کوروں', 'علاقے', 'ہوگئی', 'ًبگسیر', 'هتعلق', 'ہوئی', 'هڑا', 'لوسہ', 'گرد', 'کورٍ', 'علاوٍ', 'ہوگئے', 'ًطجت', 'هسترم', 'ہوئے', 'هڑًب', 'لو', 'گروپ',
                  'کورے', 'عووهباً', 'ہوگیب', 'ًقطہ', 'هسترهہ', 'ہوتی', 'هڑے', 'لوگ', 'گروٍ', 'کوطي', 'عووهی', 'ہوًی', 'ًکبلٌب', 'هسطوش', 'ہوتے', 'هہرثبى', 'لوگوں',
                  'گروہوں', 'کوى', 'فرد', 'ہی', 'ًکتہ', 'هختلف', 'ہوچکب', 'هیرا', 'لڑکپي', 'گٌتی', 'کوًطب', 'فی', 'یقیٌباً', 'ًو', 'هسیذ', 'ہوچکی', 'هیری', 'لی', 'لازهباً',
                  'کوًطی', 'قجل', 'یقیٌی', 'ًوخواى', 'هطئلہ', 'ہوچکے', 'هیرے', 'لیب', 'ضت', 'ثبعث', 'ہورہی', 'ًئے', 'لیں', 'ہورہب', 'ًئی', 'لیٌب', 'لیے']
    #text_list = process(raw_text, stop_words)
    
    """Creating Text List"""
    # create list having each sentence as element
    text_temp = raw_text.replace("\n", "۔")
    text_list = text_temp.split("۔")
    # print(data)
    # print(len(data))
    
    # remove punctuations from sentences
    
    for i in range(len(text_list)):
        if text_list[i] != '':
            text_list[i] = ''.join(c for c in text_list[i] if unicodedata.category(c) != 'Po')
    
    # Remove stopwords
    for i in range(len(text_list)):
        text_list[i] = remove_stopwords(text_list[i].split(" "), stop_words)
        
        
    """Finding Word Frequencies"""
    word_freq = {}
    
    for sent in text_list:
        for word in sent.split(" "):
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    
    """Assigning word frequencies"""
    result_temp = []
    sent_no = 0
    for i in text_list:
        sent_dict = {}
        score = 0
        for j in i.split(" "):
            if j not in sent_dict: # only unique words, is best strategy
                sent_dict[j] = word_freq[j]
                score += word_freq[j]
        result_temp.append([sent_no, score, sent_dict])
        sent_no += 1
        
    sorted_list = sorted(result_temp, key=lambda x: x[1])
    
    
    """Creating raw text list"""
    raw_text_temp = raw_text.replace("\n","۔")
    raw_text_list = raw_text_temp.split("۔")
    
    
    """Getting sentences from original text according to max score"""
    # Getting indices of max score sentences
    indices = []
    for i in range(n_sentences):
        index_temp = sorted_list[-(i+1)][0]
        indices.append(index_temp)
    # Getting sentences
    summary_sentences = []
    for i in indices:
        summary_sentences.append(raw_text_list[i])

    
    with open('result.txt', 'w') as file:
        for i in summary_sentences:
            file.write(f"{i}\n")
    
    return summary_sentences

        

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

ExtractiveTextSummarization(text, 4)
        
    
    