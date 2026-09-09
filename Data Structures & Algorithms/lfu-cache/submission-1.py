class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> [val, freq]
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict(key: None)

    def _update_freq(self, key: int, val: int = None) -> int:
        """Helper to increment a key's frequency and move it to the new frequency bucket."""
        curr_val, freq = self.key_to_val_freq[key]
        val = val if val is not None else curr_val
        
        # Remove key from its current frequency group
        del self.freq_to_keys[freq][key]
        
        # Advance min_freq if the current lowest frequency bucket becomes empty
        if self.min_freq == freq and not self.freq_to_keys[freq]:
            self.min_freq += 1
            
        # Update metadata and push key into the new frequency bucket (marked as most recent)
        self.key_to_val_freq[key] = [val, freq + 1]
        self.freq_to_keys[freq + 1][key] = None
        return val

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        return self._update_freq(key)

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # Case 1: Key exists -> update value and bump frequency
        if key in self.key_to_val_freq:
            self._update_freq(key, value)
            return

        # Case 2: Cache is full -> pop LRU key from min_freq group (first item in OrderedDict)
        if len(self.key_to_val_freq) == self.cap:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        # Case 3: Insert new key with freq = 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1