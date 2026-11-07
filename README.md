<div align="center">

<img src=".github/assets/banner.jpg" alt="LeetCode-Submissions: NeetCode.io and LeetCode.com solutions synced to GitHub" width="100%" />

# LeetCode & NeetCode Solutions

**Every problem I've solved on [NeetCode.io](https://neetcode.io) and [LeetCode](https://leetcode.com/u/HelionImperion/), synced here automatically.**

<a href="https://leetcode.com/u/HelionImperion/"><img src="https://leetcard.jacoblin.cool/HelionImperion?theme=dark&font=Fira%20Code&ext=heatmap" alt="LeetCode stats for HelionImperion" /></a>

![Last commit](https://img.shields.io/github/last-commit/AbdulDevHub/Leetcode-Submissions?style=flat-square&label=last%20solved)
![Top language](https://img.shields.io/github/languages/top/AbdulDevHub/Leetcode-Submissions?style=flat-square)
[![Stats](https://img.shields.io/github/actions/workflow/status/AbdulDevHub/Leetcode-Submissions/update-readme.yml?style=flat-square&label=stats)](../../actions/workflows/update-readme.yml)

</div>

---

## 📊 Progress by topic

Topics follow the [NeetCode roadmap](https://neetcode.io/roadmap). This section rebuilds itself whenever new solutions land.

<!-- STATS:START -->
![Solved](https://img.shields.io/badge/Solved-217-2ea043?style=for-the-badge) ![Easy](https://img.shields.io/badge/Easy-108-00b8a3?style=for-the-badge) ![Medium](https://img.shields.io/badge/Medium-93-ffc01e?style=for-the-badge) ![Hard](https://img.shields.io/badge/Hard-16-ff375f?style=for-the-badge) ![NeetCode 150](https://img.shields.io/badge/NeetCode%20150-53/150-7c3aed?style=for-the-badge)

| Topic | Solved | Easy | Medium | Hard | NeetCode 150 |
|---|:-:|:-:|:-:|:-:|---|
| Arrays & Hashing | **72** | 50 | 20 | 2 | `██████████` 9/9 |
| Two Pointers | **23** | 11 | 11 | 1 | `██████████` 5/5 |
| Sliding Window | **18** | 3 | 12 | 3 | `██████████` 6/6 |
| Stack | **22** | 8 | 11 | 3 | `█████████░` 6/7 |
| Binary Search | **26** | 9 | 13 | 4 | `██████████` 7/7 |
| Linked List | **24** | 7 | 14 | 3 | `██████████` 11/11 |
| Trees | **23** | 13 | 10 | 0 | `██████░░░░` 9/15 |
| Heap / Priority Queue | **1** | 0 | 1 | 0 | `░░░░░░░░░░` 0/7 |
| 1-D Dynamic Programming | **1** | 1 | 0 | 0 | `░░░░░░░░░░` 0/12 |
| Greedy | **2** | 1 | 1 | 0 | `░░░░░░░░░░` 0/8 |
| Math & Geometry | **2** | 2 | 0 | 0 | `░░░░░░░░░░` 0/8 |
| Bit Manipulation | **3** | 3 | 0 | 0 | `░░░░░░░░░░` 0/7 |

**Languages:** Python (503 files) · TypeScript (11 files)
<!-- STATS:END -->

---

## ⚙️ How it stays in sync

| Source | How | When |
|---|---|---|
| **NeetCode.io** | NeetCode's GitHub integration commits each submission | Instantly, on every submit |
| **LeetCode.com** | [`leetcode-sync`](https://github.com/joshcai/leetcode-sync) GitHub Action pulls the latest accepted solution per problem | 1st of every month, 08:00 UTC (or run it manually from **Actions**) |
| **This README** | A small Python script counts solutions by topic and difficulty | After every push and every LeetCode sync |

## 📁 Repository layout

```
Leetcode-Submissions/
├── Data Structures & Algorithms/      ← NeetCode solutions
│   └── <problem>/submission-<n>.<ext> ← every submission, oldest first
├── LeetCode-Problems/                 ← LeetCode solutions
│   └── <id>-<problem>/                ← problem statement + latest accepted solution
└── .github/
    ├── workflows/                     ← LeetCode sync + README stats
    └── scripts/update_readme.py       ← builds the progress table
```

---

## 🔑 Fixing the LeetCode sync

If the **Sync LeetCode** action fails with this error, the LeetCode login cookies have expired (they last a few weeks):

```
TypeError: response.data.data.submissionList.submissions is not iterable
```

To fix it (about 2 minutes):

1. Log in to [leetcode.com](https://leetcode.com) in your browser.
2. Open DevTools (`F12`), then go to **Application** → **Cookies** → `https://leetcode.com`.
3. Copy the values of `LEETCODE_SESSION` and `csrftoken`.
4. In this repo, open **Settings** → **Secrets and variables** → **Actions** and update:
   - `LEETCODE_SESSION` → the `LEETCODE_SESSION` cookie
   - `LEETCODE_CSRF_TOKEN` → the `csrftoken` cookie
5. Go to **Actions** → **Sync LeetCode** → **Run workflow** to sync right away.

> [!TIP]
> Copy fresh cookies from a session you stay logged in to. Logging out of LeetCode may invalidate them early.

<details>
<summary><b>Stats table shows a problem in the wrong place?</b></summary>

<br>

NeetCode renames some problems (for example `two-integer-sum` is LeetCode's `two-sum`). If the stats action logs `No LeetCode match`, add the pair to [`.github/scripts/neetcode-aliases.json`](.github/scripts/neetcode-aliases.json).

</details>

---

<div align="center">
<sub>NeetCode sync by <a href="https://neetcode.io">NeetCode GitHub Integration</a> · LeetCode sync by <a href="https://github.com/joshcai/leetcode-sync">leetcode-sync</a> · Stats card by <a href="https://github.com/JacobLinCool/LeetCode-Stats-Card">LeetCode-Stats-Card</a></sub>
</div>
