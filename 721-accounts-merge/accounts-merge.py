class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        parent = {}

        def makeset(x):
            if x not in parent:
                parent[x] = x
        
        def find(x):
            while parent[x] != x:
                x = find(parent[x])
            return x

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                parent[rooty] = rootx
        
        email_name = {}
        for account in accounts:
            name = account[0]
            root_email = account[1]
            makeset(root_email)
            email_name[root_email] = name

            for email in account[1:]:
                makeset(email)
                union(root_email, email)
                email_name[email] = name

        emails_group = collections.defaultdict(list)
        for email in email_name:
            root = find(email)
            emails_group[root].append(email)
        
        result = []
        for root, emails in emails_group.items():
            name = email_name[root]
            result.append([name] + sorted(emails))

        return result

        

        
        