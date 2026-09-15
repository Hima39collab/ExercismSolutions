def find_anagrams(word, candidates):
    result = []

    for candidate in candidates:
        if candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
                result.append(candidate)

    return result

        
        
        
