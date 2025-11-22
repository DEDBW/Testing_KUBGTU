class StringManipulator:
    @staticmethod
    def replace_substring(original_str, old_sub, new_sub):
        result = []
        i = 0
        old_len = len(old_sub)

        while i < len(original_str):
            if original_str[i:i + old_len] == old_sub:
                result.append(new_sub)
                i += old_len
            else:
                result.append(original_str[i])
                i += 1

        return ''.join(result)
