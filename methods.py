# Methods

class MethodExamples:

    # this_can_be_accessed_easily = "Hi, I am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!" # this is for a classs variable , for a method we would use two underscores
    # we have protected it by putting it into this initialise block
    # def get_this_can_be_accessed_easily(self):
    #     return self.this_can_be_accessed_easily
    #
    # def get_this_can_be_accessed_easily(self, value_to_be_set):
    #     return self.this_can_be_accessed_easily = value_to_be_set

# x = MethodExamples()
#
# print(x.this_can_be_accessed_easily)
# x.this_can_be_accessed_easily = "I have been changed!"
# print(x.this_can_be_accessed_easily)  # we don't want to overwrite everything



# Public and private


x = MethodExamples()

print(x.get_this_can_be_accessed_easily()) # for methods we use double underscore
x.set_this_can_be_accessed_easily("I have been changed!")
print(x.get_this_can_be_accessed_easily())  # we don't want to overwrite everything