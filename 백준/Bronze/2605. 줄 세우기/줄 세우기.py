number = int(input())
card_list = list(map(int, input().split(" ")))

end_list = []
for count in range(number):
    end_list.insert(card_list[count], count + 1)
    
end_string = ""
for count in range(number):
    end_string = str(end_list[count]) + " " + end_string

print(end_string)