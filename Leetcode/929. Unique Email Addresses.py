class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_emails = []
        for i in range(len(emails)):
            [local, domain] = emails[i].split('@')
            local_new = ''
            for j in range(len(local)):
                if local[j] == '.':
                    pass
                elif local[j] == '+':
                    break
                else:
                    local_new += local[j]
            new_emails.append(local_new + domain)
        new_emails = list(set(new_emails))
        return len(new_emails)

