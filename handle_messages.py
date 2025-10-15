import re
# from underthesea import word_tokenize

def clean_message(msg):
    msg = str(msg).lower()
    msg = re.sub(r"http\S+|www\S+", " ", msg)
    msg = re.sub(r"[!?]+", " ! ", msg)  # Giữ lại dấu '!' như tín hiệu cảm xúc
    msg = re.sub(r"<.*?>", " ", msg)
    msg = re.sub(r"[^a-zA-ZÀ-ỹà-ỹ0-9\s!]", " ", msg)

    msg = re.sub(r"\b(?:not|no|never|n't)\s+(\w+)", r"not_\1", msg)
    msg = re.sub(r"\b(don t like|dont like|didn t like|hate it)\b", " not_like ", msg)

    msg = re.sub(r"\b(okie|oke|okey|oki|ok)\b", "okay", msg)

    msg = re.sub(r"\b(gr8)\b", "great", msg)
    msg = re.sub(r"\b(luv)\b", "love", msg)
    msg = re.sub(r"\b(thanx|thx|thanks)\b", "thank", msg)
    msg = re.sub(r"\b(awsm|awsome)\b", "awesome", msg)
    msg = re.sub(r"\b(wtf)\b", "bad", msg)
    msg = re.sub(r"\b(omg)\b", "surprised", msg)
    msg = re.sub(r"\b(sux|sucks)\b", "bad", msg)

    msg = re.sub(r"[^\w\s]", " ", msg)
    msg = re.sub(r"\s+", " ", msg).strip()
    return msg


# def clean_message(msg: str) -> str:
#     if pd.isna(msg):
#         return ""
#     msg = msg.lower()
#     msg = re.sub(r"http\S+|www\S+", "", msg)
#     msg = re.sub(r"@\w+|#\w+", "", msg)
#     msg = re.sub(r"[!?]+", " ! ", msg)
#     msg = re.sub(r"[^a-zA-ZÀ-ỹà-ỹ0-9\s]", " ", msg)
#     msg = re.sub(r"\s+", " ", msg).strip()
#     msg = word_tokenize(msg, format="text")
#
#     msg = msg.replace("ko", "không").replace("k", "không")
#     msg = msg.replace("okie", "ok").replace("oke", "ok").replace("okey", "ok").replace("oki", "ok")
#     msg = msg.replace("good", "tốt").replace("wonderful", "tuyệt vời")
#     msg = msg.replace("bad", "tệ").replace("terrible", "tồi tệ").replace("horrible", "kinh khủng")
#
#     return msg
#
# # =============================
# # Stopwords Tiếng Việt
# # =============================
# stopwords_vi = {
#     "và", "là", "có", "của", "trong", "với", "cho", "được", "này", "rất",
#     "thì", "lại", "đã", "sẽ", "không", "nên", "vì", "ở", "khi", "nhưng", "cũng",
#     "rằng", "một", "các", "như", "để", "tôi", "bạn", "chúng", "ta", "nó", "họ",
#     "đó", "kia", "ấy", "nào", "vậy", "vâng", "ừ", "ờ", "ừm", "nhỉ", "ha", "à",
#     "dạ", "chứ", "thôi", "đi", "nha", "nhé", "cơ", "ơi", "haiz", "haha", "hihi",
#     "hj", "kk", "với", "vẫn", "đang", "đều", "được", "từ", "bị", "đến", "lúc",
#     "trước", "sau", "còn", "nữa", "luôn", "thật", "ra", "tại", "đây", "đấy",
#     "điều", "gì", "ai", "đâu", "nào", "sao", "chắc", "rồi", "cứ", "vì", "nên",
#     "cảm", "ơn", "xin", "vui", "lòng"
# }
#
# # =============================
# # Stopwords Tiếng Anh
# # =============================
# stopwords_en = {
#      "the", "is", "are", "was", "were", "a", "an", "this", "that", "in", "on",
#     "of", "for", "and", "or", "to", "with", "by", "from", "at", "as", "be",
#     "can", "could", "should", "would", "do", "does", "did", "not", "no", "yes",
#     "if", "when", "what", "who", "how", "why", "about", "it", "we", "they",
#     "you", "he", "she", "them", "their", "our", "us", "my", "your", "yours",
#     "mine", "his", "her", "hers", "its", "then", "there", "here", "out", "up",
#     "down", "so", "very", "really", "just", "only", "too", "because", "although",
#     "though", "while", "but", "also", "been", "have", "has", "having", "had",
#     "don", "doesn", "didn", "will", "won", "shall", "shouldn", "must",
#     "might", "may", "perhaps", "maybe", "yes", "no", "uh", "um", "well", "hmm"
# }
#
# # =============================
# # Gộp thành list để sklearn sử dụng
# # =============================
# custom_stopwords = list(stopwords_vi.union(stopwords_en))