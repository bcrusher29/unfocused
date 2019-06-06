# -*- coding: utf-8 -*-

'''
    Still i Rise Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
from resources.lib.modules import cache

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')

        if not control.setting('lists.widget') == '0':
            self.addDirectoryItem(32003, 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
            self.addDirectoryItem(32004, 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem(32006, 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')

        self.addDirectoryItem(32007, 'channels', 'channels.png', 'DefaultMovies.png')

        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        if downloads == True:
            self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')

        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenres', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('Leather Faces Love Stories', 'lflsNavigator', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem('Dracula And Friends', 'Dafmnav', 'drac.png', 'DefaultMovies.png')
        self.addDirectoryItem('Laughing IT Up', 'lhmovies', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem('Jasons Camping Activites', 'jcamNavigator', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem('Haddonfield Murder Mysteries', 'hadmovNavigator', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem('Jigsaws PlayTime', 'jptmovNavigator', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem('Deep Space', 'deepmovNavigator', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem('NightMare Reborn', 'nightmovNavigator', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem('GhostTown', 'gtmovNavigator', 'gticon.png', 'DefaultMovies.png')

        self.addDirectoryItem(32012, 'movieYears', 'years.png', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', 'people.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguages', 'languages.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        self.addDirectoryItem(32017, 'movies&url=trending', 'people-watching.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'movies&url=views', 'most-voted.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', 'box-office.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()
##################################lfls################################
    def lfls(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenresdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYearsdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguagesdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificatesdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'dkmov&url=populardrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'dkmov&url=viewsdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'dkmov&url=boxofficedrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'dkmov&url=oscarsdrama', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'dkmov&url=theatersdrama', 'lf.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32011, 'movieGenresrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYearsrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguagesrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificatesrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32017, 'dkmov&url=trendingrom', 'lf.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'dkmov&url=popularrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'dkmov&url=viewsrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'dkmov&url=boxofficerom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'dkmov&url=oscarsrom', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'dkmov&url=theatersrom', 'lf.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
####################################################################################
##################################lfls################################
    def gtm(self, lite=False):
        self.addDirectoryItem(32011, 'gtmovGenres', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'gtmovYears', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'gtmovLanguages', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'gtmovCertificates', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'wwmovies&url=popular', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'wwmovies&url=views', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'wwmovies&url=boxoffice', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'wwmovies&url=oscars', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'wwmovies&url=theaters', 'gticon.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'wwmovies&url=trending', 'gticon.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
####################################################################################
##################################lfls################################
    def dafm(self, lite=False):
        self.addDirectoryItem('50s to 60s Movies', 'movieGenres50', 'drac.png', 'Defaultmovies.png')
        self.addDirectoryItem('60s to 70s Movies', 'movieGenres60', 'drac.png', 'Defaultmovies.png')
        self.addDirectoryItem('70s to 80s Movies', 'movieGenres70', 'drac.png', 'Defaultmovies.png')		
        self.addDirectoryItem('80s to 90s Movies', 'movieGenres80', 'drac.png', 'Defaultmovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def hfmm(self, lite=False):
        self.addDirectoryItem(32011, 'hadmovGenres', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'hadmovYears', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'hadmovLanguages', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'hadmovCertificates', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'hmmm&url=popular', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'hmmm&url=views', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'hmmm&url=boxoffice', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'hmmm&url=oscars', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'hmmm&url=theaters', 'hdd.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'hmmm&url=trending', 'hdd.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def nightmov(self, lite=False):
        self.addDirectoryItem(32011, 'nightmovGenres', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'nightmovYears', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'nightmovLanguages', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'nightmovCertificates', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'nmaremov&url=popular', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'nmaremov&url=views', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'nmaremov&url=boxoffice', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'nmaremov&url=oscars', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'nmaremov&url=theaters', 'fre.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'nmaremov&url=trending', 'fre.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def jcam(self, lite=False):
        self.addDirectoryItem(32011, 'jcamGenres', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'jcamYears', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'jcamLanguages', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'jcamCertificates', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'apmovies&url=popular', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'apmovies&url=views', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'apmovies&url=boxoffice', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'apmovies&url=oscars', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'apmovies&url=theaters', 'jas.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'apmovies&url=trending', 'jas.png', 'DefaultRecentlyAddedMovies.png')
	
        self.endDirectory()
####################################################################################
##################################lfls################################
    def jptm(self, lite=False):
        self.addDirectoryItem(32011, 'jptmovGenres', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'jptmovYears', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'jptmovLanguages', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'jptmovCertificates', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'odintoons&url=popular', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'odintoons&url=views', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'odintoons&url=boxoffice', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'odintoons&url=oscars', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'odintoons&url=theaters', 'js.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'odintoons&url=trending', 'js.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def deepmov(self, lite=False):
        self.addDirectoryItem(32011, 'deepmovGenres', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'deepmovYears', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'deepmovLanguages', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'deepmovCertificates', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'asmovies&url=popular', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'asmovies&url=views', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'asmovies&url=boxoffice', 'dss.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'asmovies&url=oscars', 'ds.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'asmovies&url=theaters', 'ds.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'asmovies&url=trending', 'ds.png', 'DefaultRecentlyAddedMovies.png')
	
        self.endDirectory()
######################################################################################################################lfls################################
    def liumov(self, lite=False):
        self.addDirectoryItem(32011, 'movieGenreslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYearslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'movieLanguageslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificateslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32018, 'lhmovies&url=popular', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'lhmovies&url=views', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'lhmovies&url=boxoffice', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'lhmovies&url=oscars', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32022, 'lhmovies&url=theaters', 'liu.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'lhmovies&url=trending', 'liu.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
####################################################################################
    def tvshows(self, lite=False):
        self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem('Leather Faces Love Stories', 'lflstvNavigator', 'lf.png', 'DefaultMovies.png')
        self.addDirectoryItem('Dracula And Friends', 'Daftvnav', 'drac.png', 'DefaultMovies.png')
        self.addDirectoryItem('Laughing IT up', 'lhtv', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem('Jasons Camping Activites', 'jcatvNavigator', 'jas.png', 'DefaultMovies.png')
        self.addDirectoryItem('Haddonfield Murder Mysteries', 'hadtvnav', 'hdd.png', 'DefaultMovies.png')
        self.addDirectoryItem('Jigsaws PlayTime', 'jpttvnav', 'js.png', 'DefaultMovies.png')
        self.addDirectoryItem('Deep Space', 'deeptvnav', 'dsds.png', 'DefaultMovies.png')
        self.addDirectoryItem('NightMare ReBorn', 'nighttvnav', 'fre.png', 'DefaultMovies.png')
        self.addDirectoryItem('Ghost Town', 'gttvnav', 'gticon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguages', 'languages.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificates', 'certificates.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'tvshows&url=trending', 'people-watching.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'most-voted.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', 'calendar.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()

##################################lfls################################
    def lflstv(self, lite=False):
        self.addDirectoryItem('tv', 'tvGenresdrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguagesdrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'dktvshows&url=populardrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'dktvshows&url=ratingdrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'dktvshows&url=viewsdrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'dktvshows&url=airingdrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'dktvshows&url=premieredrama', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32011, 'tvGenresrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworksrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'tvLanguagesrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificatesrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'dktvshows&url=trendingrom', 'lf.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'dktvshows&url=popularrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'dktvshows&url=ratingrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'dktvshows&url=viewsrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'dktvshows&url=airingrom', 'lf.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'dktvshows&url=premiererom', 'lf.png', 'DefaultTVShows.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def gttv(self, lite=False):
        self.addDirectoryItem('tv', 'gttvGenres', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'gttvNetworks', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'gttvLanguages', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'wwtvshows&url=popular', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'wwtvshows&url=rating', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'wwtvshows&url=views', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'wwtvshows&url=airing', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'wwtvshows&url=premiere', 'gticon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'gttvYears', 'gticon.png', 'DefaultMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def daftv(self, lite=False):
        self.addDirectoryItem('50s to 60s TV Shows', 'tvGenres50', 'drac.png', 'Defaultmovies.png')		
        self.addDirectoryItem('60s to 70s TV Shows', 'tvGenres60', 'drac.png', 'Defaultmovies.png')		
        self.addDirectoryItem('70s to 80s TV Shows', 'tvGenres70', 'drac.png', 'Defaultmovies.png')		
        self.addDirectoryItem('80s to 90s TV Shows', 'tvGenres80', 'drac.png', 'Defaultmovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def hfmmtv(self, lite=False):
        self.addDirectoryItem(32011, 'hadtvGenres', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'hadtvNetworks', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'hadtvLanguages', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'hmmtv&url=popular', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'hmmtv&url=rating', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'hmmtv&url=views', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'hmmtv&url=airing', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'hmmtv&url=premiere', 'hdd.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'hadtvYears', 'hdd.png', 'DefaultMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def nighttv(self, lite=False):
        self.addDirectoryItem(32011, 'nighttvGenres', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'nighttvNetworks', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'nighttvLanguages', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'nmaretv&url=popular', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'nmaretv&url=rating', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'nmaretv&url=views', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'nmaretv&url=airing', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'nmaretv&url=premiere', 'fre.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'nighttvYears', 'fre.png', 'DefaultMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def jcatv(self, lite=False):
        self.addDirectoryItem(32011, 'jcatvGenres', 'jas.pngjas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'jcatvNetworks', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'jcatvLanguages', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'aptvshows&url=popular', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'aptvshows&url=rating', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'aptvshows&url=views', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'aptvshows&url=airing', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'aptvshows&url=premiere', 'jas.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'jcatvYears', 'jas.png', 'DefaultMovies.png')

        self.endDirectory()
####################################################################################
##################################lfls################################
    def jpttv(self, lite=False):
        self.addDirectoryItem(32011, 'jpttvGenres', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'jpttvNetworks', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'jpttvLanguages', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'odintvtoons&url=popular', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'odintvtoons&url=rating', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'odintvtoons&url=views', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'odintvtoons&url=airing', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'odintvtoons&url=premiere', 'js.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'jpttvYears', 'js.png', 'DefaultMovies.png')
        self.endDirectory()
####################################################################################
##################################lfls################################
    def deeptv(self, lite=False):
        self.addDirectoryItem(32011, 'deeptvGenres', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'deeptvNetworks', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32014, 'deeptvLanguages', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'astvshows&url=popular', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'astvshows&url=rating', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'astvshows&url=views', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'astvshows&url=airing', 'dsds.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'astvshows&url=premiere', '.dsdspng', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'deeptvYears', 'dsds.png', 'DefaultMovies.png')

        self.endDirectory()
######################################################################################################################lfls################################
    def liutv(self, lite=False):
        self.addDirectoryItem(32015, 'tvCertificateslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32011, 'tvGenreslh', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32012, 'tvYearslh', 'liu.png', 'DefaultMovies.png')
        self.addDirectoryItem(32014, 'tvLanguageslh', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32018, 'lhtvshows&url=popular', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'lhtvshows&url=rating', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'lhtvshows&url=views', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'lhtvshows&url=airing', 'liu.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'lhtvshows&url=premiere', 'liu.png', 'DefaultTVShows.png')
        self.endDirectory()
####################################################################################
    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32556, 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32604, 'clearCacheSearch', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32558, 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32559, control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(32560, control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

        self.endDirectory()

    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheMeta(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_meta()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheProviders(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_providers()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheAll(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_all()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)

    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
