from quran import Quran
qur = Quran()

# All the methods returns a dictionary object

# Getting all Recitations
qur.get_recitations

# Getting all available Translations
qur.get_translations()

# Getting all avalailable Languages
qur.get_languages()

# Getting all Tafsirs available in this api
qur.get_tafsirs()

# Getting all Chapters names
qur.get_chapter(6, info=True, language='ur') # Keyworded arguments are optional

# Getting all the Verses from a chapter
qur.get_verses(6)