# Computer-Architecture 

## 1) Toggle LFU LRU Cache Replacement Policy:
###         The Least Recently Used (LRU) is a cache replacement policy which evicts the block which was least recently used, that is the oldest block used. The Least Frequently Used (LFU) is a cache replacement policy which replaces a block which has the least frequency count. But, LFU policy has a disadvantage of keeping unwanted blocks with high frequency in the list. To overcome this, a new cache replacement policy T-LFU-LRU (Toggle-LFU-LRU) is proposed, which periodically toggles from LFU to LRU to evict the unwanted high frequency block. The goal of this experiment is to implement LFU and T-LFU-LRU in Simplescalar simulator and evaluate T-LFU-LRU and LFU against LRU for specific benchmarks.

## 2) Branch Predictor in Python:
###         This is a simulator to simulate two simple conditional branch predicators. The first predictor has 32 1-bit predictors, saving the action of only the last branch to predict the outcome of the next branch. The second predictor uses 16 2-bit counters to predict branches. 

## 3) Column Associative Cache:
###         This is a simulator in Python which mimics a Column Associative Cache Model.
