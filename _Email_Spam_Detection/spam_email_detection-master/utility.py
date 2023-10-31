# -*- coding: utf-8 -*-
import email

def read_email(labels, DATA_DIR):
    X = []
    y = []
    for i in range(len(labels)):
        filename = 'inmail.' + str(i+1)
        filepath = DATA_DIR + filename
        email_str = extract_email_text(filepath)
        X.append(email_str)
        y.append(labels[filename])
    return X, y

def extract_email_text(path):
    
    with open(path, errors='ignore') as f:
        msg = email.message_from_file(f)
        
    if not msg:
        return ""
    
    subject = msg["subject"]
    
    if not subject:
        return ""
    
    body = ' '.join(m for m in flatten_to_string(msg.get_payload()) if type(m) == str)
    
    if not body:
        body = ""
    
    return subject + ' ' + body


def flatten_to_string(parts):
    ret = []
    
    if type(parts) == str:
        ret.append(parts)
    elif type(parts) == list:
        for part in parts:
            ret += flatten_to_string(part)
    elif parts.get_content_type == 'text/plain':
        ret += parts.get_payload()
        
    return ret