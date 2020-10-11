"""
Topics: | String |
"""

class Solution:

    def numUniqueEmails(self, emails):
        """
        Time:  O(ne)  [where n = len(emails), e = len(longest email)]
        Space: O(n)
        """
        unique_emails = set()
        for email in emails:
            unique_emails.add(self.process_address(email))
        return len(unique_emails)

    def process_address(self, email):
        local, domain = email.split('@')  # Assumes exactly one '@'
        plus_index = local.find('+')
        if plus_index != -1:
            local = local[: plus_index]
        local = local.replace('.', '')
        return local + '@' + domain
