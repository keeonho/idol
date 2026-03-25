# Changes made to idol.py

## Major Changes:
1. **Username Display in Debut Announcements and Member Lists**: Updated to show in format "stage_name (@username)".

2. **Bubble Post Format Update**: Changed format to:
   "DDMMYY [CARENT UPDATE]\n\n[#STAGENAME]\n[EMOJI] : [MESSAGE]\n\n[EMOJI] // @CARENTERTAINMENT"

3. **Vote Duplicate Prevention**: Implemented check against the database before allowing votes to prevent duplicates.

4. **Emoji Selector for Bubble Posts**: Added functionality for users to select emojis from a preset list for bubble posts.

5. **Fix for WHERE Clause Errors**: Fixed errors in PATCH and DELETE operations by ensuring proper filters are applied.

6. **Pagination Support for Group Listings**: Added support for pagination to make group listings more manageable.

7. **Log Messages Update**: Changed all log messages to now include the user's username along with their name.

8. **Character Count Validation**: Added validation to ensure bubble messages do not exceed character limits.