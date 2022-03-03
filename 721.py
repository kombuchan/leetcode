# Accounts Merge
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = {}
        for num, i in enumerate(accounts):
            name = i[0]
            if name in users: users[name + "_dup" + str(num)] = set(i[1:])
            else: users[name] = set(i[1:])
        visited = set()
        
        length,n = len(users),len(users)
        
        for i in users:
            for email in users[i]:
                if email in visited:
                    original = i.split("_dup")[0]
                    for j in users[i]: users[original].add(j)
                    users[i] = ""
                else: visited.add(email)
        
        ret = []
        for i in users:
            name = i
            if users[i] == "": continue
            if "_dup" in name: 
                name = i.split("_dup")[0]
            ret.append([name] + sorted(list(users[i])))
            
        return ret 
        