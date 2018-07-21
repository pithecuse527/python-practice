def max_len(list) :
    m_len = list[0]
    for word in list :
        if len(word) > len(m_len):
            m_len = word
    return m_len

def dic_sort(list_) :
    al_str = ("AaBbCcDdEeFfGgHhIiJjKk\
              LlMmNnOoPpQqRrSsTtUuVv\
              WwXxYyZz")
    al_list = list(al_str)

    list_len = len(list_)

    tmp_list = []
    for i in range(list_len):
        tmp = ""
        for alphabet in list_[i]:
            tmp = tmp + str(al_list.index(alphabet))
        tmp_list.append(tmp)

    tmp_list_len = len(tmp_list)
    print(tmp_list)
    for j in range(tmp_list_len-1) :
        for k in range(len(tmp_list[j])) :
            for l in range(j+1, tmp_list_len) :
                print(int(tmp_list[j][k]))
                print(int(tmp_list[l][k]))
                #if (int(tmp_list[j][k])) > (int(tmp_list[l][k]))
                #if int(k) > int(tmp_list[l]):
 #                   tmp_list[j], tmp_list[l] = tmp_list[l], tmp_list[j]
   # print(tmp_list_len)
            
def dic_sort2(list):

    dic_fast = list[0]
    for word in list :
        if dic_fast > word:
            dic_fast = word
    return dic_fast
        
def main():

    list = []
    tmp = ""
    while True:
        print("입력을 중단하려면 -1을 입력하시오.\n")
        tmp = input("단어를 입력하시오.")
        if tmp == "-1":
            break
        list.append(tmp)

    print("가장 긴 단어는 \'" + max_len(list) + "\' 입니다.")
    print("사전식 순서가 가장 빠른 단어는 \'" + dic_sort2(list) + "\' 입니다.")


main()
    
    

    
        
