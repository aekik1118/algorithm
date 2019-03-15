record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    answer = []
    buffer = []

    chatroom = dict()

    for i in record:
        tmp = i.split()
        op = tmp[0]
        uid = tmp[1]

        if op == "Enter":
            nic = tmp[2]
            chatroom[uid] = nic
            buffer.append([uid, "님이 들어왔습니다."])
        elif op == "Leave":
            buffer.append([uid, "님이 나갔습니다."])
        else:
            nic = tmp[2]
            chatroom[uid] = nic

    for i in buffer:
        answer.append(chatroom[i[0]] + i[1])

    return answer