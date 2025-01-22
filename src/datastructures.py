class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    def add_member(self, member):
        member["last_name"] = self.last_name
        if "id" not in member:
            member["id"] = self._generateId()
        if "lucky_numbers" not in member:
            member["lucky_numbers"] = []
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for position, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(position)
                return True
        return False



    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member
            
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
