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


import urlparse,sys,urllib

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0


if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()
    
elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'smuSettings':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

#######################Dark Love#########################################

elif action == 'lflsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().lfls()
	
elif action == 'lflstvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().lflstv()
	
elif action == 'moviedramaNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().moviesdrama()

elif action == 'movieromNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().moviesrom()


elif action == 'movieGenresdrama':
    from resources.lib.indexers import dkmov
    dkmov.movies().genresdrama()
	
elif action == 'movieGenresrom':
    from resources.lib.indexers import dkmov
    dkmov.movies().genresrom()

	
	
elif action == 'movieLanguagesdrama':
    from resources.lib.indexers import dkmov
    dkmov.movies().languagesdrama()

elif action == 'movieLanguagesrom':
    from resources.lib.indexers import dkmov
    dkmov.movies().languagesrom()

elif action == 'movieCertificatesdrama':
    from resources.lib.indexers import dkmov
    dkmov.movies().certificationsdrama()

elif action == 'movieCertificatesrom':
    from resources.lib.indexers import dkmov
    dkmov.movies().certificationsrom()

elif action == 'movieYearsdrama':
    from resources.lib.indexers import dkmov
    dkmov.movies().yearsdrama()

elif action == 'movieYearsrom':
    from resources.lib.indexers import dkmov
    dkmov.movies().yearsrom()

elif action == 'tvNavigatordrama':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshowsdrama()

elif action == 'tvNavigatorrom':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshowsrom()

elif action == 'tvYearsdrama':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().yearsdrama()

elif action == 'tvYearsrom':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().yearsrom()

elif action == 'tvGenresdrama':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().genresdrama()

elif action == 'tvGenresrom':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().genresrom()

elif action == 'tvLanguagesdrama':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().languagesdrama()

elif action == 'tvLanguagesrom':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().languagesrom()

elif action == 'tvCertificatesdrama':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().certificationsdrama()

elif action == 'tvCertificatesrom':
    from resources.lib.indexers import dktvshows
    dktvshows.tvshows().certificationsrom()
##################################action packed###################################3

elif action == 'jcamNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().jcam()
	
elif action == 'jcamGenres':
    from resources.lib.indexers import apmovies
    apmovies.movies().genres()

elif action == 'jcamLanguages':
    from resources.lib.indexers import apmovies
    apmovies.movies().languages()

elif action == 'jcamCertificates':
    from resources.lib.indexers import apmovies
    apmovies.movies().certifications()

elif action == 'jcamYears':
    from resources.lib.indexers import apmovies
    apmovies.movies().years()


elif action == 'jcatvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().jcatv()

elif action == 'jcatvYears':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().years()

elif action == 'jcatvGenres':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().genres()

elif action == 'jcatvLanguages':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().languages()


elif action == 'jcatvCertificates':
    from resources.lib.indexers import aptvshows
    aptvshows.tvshows().certifications()
################################classics######################################################
elif action == 'Dafmnav':
    from resources.lib.indexers import navigator
    navigator.navigator().dafm()

elif action == 'Daftvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().daftv()

elif action == 'movieGenres50':
    from resources.lib.indexers import mcmovies
    mcmovies.movies().genres50()
	
elif action == 'movieGenres60':
    from resources.lib.indexers import mcmovies
    mcmovies.movies().genres60()
	
elif action == 'movieGenres70':
    from resources.lib.indexers import mcmovies
    mcmovies.movies().genres70()
	
elif action == 'movieGenres80':
    from resources.lib.indexers import mcmovies
    mcmovies.movies().genres80()

elif action == 'tvGenres50':
    from resources.lib.indexers import mctvshows
    mctvshows.tvshows().genres50()

	
elif action == 'tvGenres50':
    from resources.lib.indexers import mctvshows
    mctvshows.tvshows().genres50()

elif action == 'tvGenres60':
    from resources.lib.indexers import mctvshows
    mctvshows.tvshows().genres60()


elif action == 'tvGenres70':
    from resources.lib.indexers import mctvshows
    mctvshows.tvshows().genres70()

elif action == 'tvGenres80':
    from resources.lib.indexers import mctvshows
    mctvshows.tvshows().genres80()
######################################3astro###########################################
elif action == 'deepmovNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().deepmov()
	
elif action == 'deepmovGenres':
    from resources.lib.indexers import asmovies
    asmovies.movies().genres()

elif action == 'deepmovLanguages':
    from resources.lib.indexers import asmovies
    asmovies.movies().languages()

elif action == 'deepmovCertificates':
    from resources.lib.indexers import asmovies
    asmovies.movies().certifications()

elif action == 'deepmovYears':
    from resources.lib.indexers import asmovies
    asmovies.movies().years()


elif action == 'deeptvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().deeptv()

elif action == 'deeptvYears':
    from resources.lib.indexers import astvshows
    astvshows.tvshows().years()

elif action == 'deeptvGenres':
    from resources.lib.indexers import astvshows
    astvshows.tvshows().genres()

elif action == 'deeptvLanguages':
    from resources.lib.indexers import astvshows
    astvshows.tvshows().languages()


elif action == 'deeptvCertificates':
    from resources.lib.indexers import astvshows
    astvshows.tvshows().certifications()

###################################BoneCrusher################################
elif action == 'nightmovNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().nightmov()
	
elif action == 'nightmovGenres':
    from resources.lib.indexers import nmaremov
    nmaremov.movies().genres()

elif action == 'nightmovLanguages':
    from resources.lib.indexers import nmaremov
    nmaremov.movies().languages()

elif action == 'nightmovCertificates':
    from resources.lib.indexers import nmaremov
    nmaremov.movies().certifications()

elif action == 'nightmovYears':
    from resources.lib.indexers import nmaremov
    nmaremov.movies().years()


elif action == 'nighttvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().nighttv()

elif action == 'nighttvYears':
    from resources.lib.indexers import nmaretv
    nmaretv.tvshows().years()

elif action == 'nighttvGenres':
    from resources.lib.indexers import nmaretv
    nmaretv.tvshows().genres()

elif action == 'nighttvLanguages':
    from resources.lib.indexers import nmaretv
    nmaretv.tvshows().languages()


elif action == 'nighttvCertificates':
    from resources.lib.indexers import nmaretv
    nmaretv.tvshows().certifications()
########################haddonfield#####################################
elif action == 'hadmovNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().hfmm()
	
elif action == 'hadmovGenres':
    from resources.lib.indexers import hmmm
    hmmm.movies().genres()

elif action == 'hadmovLanguages':
    from resources.lib.indexers import hmmm
    hmmm.movies().languages()

elif action == 'hadmovCertificates':
    from resources.lib.indexers import hmmm
    hmmm.movies().certifications()

elif action == 'hadmovYears':
    from resources.lib.indexers import hmmm
    hmmm.movies().years()


elif action == 'hadtvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().hfmmtv()

elif action == 'hadtvYears':
    from resources.lib.indexers import hmmtv
    hmmtv.tvshows().years()

elif action == 'hadtvGenres':
    from resources.lib.indexers import hmmtv
    hmmtv.tvshows().genres()

elif action == 'hadtvLanguages':
    from resources.lib.indexers import hmmtv
    hmmtv.tvshows().languages()


elif action == 'hadtvCertificates':
    from resources.lib.indexers import hmmtv
    hmmtv.tvshows().certifications()
##############################odintoons test ####################################################################
elif action == 'jptmovNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().jptm()
	
elif action == 'jptmovGenres':
    from resources.lib.indexers import odintoons
    odintoons.movies().genres()

elif action == 'jptmovLanguages':
    from resources.lib.indexers import odintoons
    odintoons.movies().languages()

elif action == 'jptmovCertificates':
    from resources.lib.indexers import odintoons
    odintoons.movies().certifications()

elif action == 'jptmovYears':
    from resources.lib.indexers import odintoons
    odintoons.movies().years()


elif action == 'jpttvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().jpttv()

elif action == 'jpttvYears':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().years()

elif action == 'jpttvGenres':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().genres()

elif action == 'jpttvLanguages':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().languages()


elif action == 'jpttvCertificates':
    from resources.lib.indexers import odintvtoons
    odintvtoons.tvshows().certifications()

##############################laughing hour###################################
elif action == 'lhmovies':
    from resources.lib.indexers import navigator
    navigator.navigator().liumov()

elif action == 'lhtv':
    from resources.lib.indexers import navigator
    navigator.navigator().liutv()

elif action == 'movieYearslh':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().years()

elif action == 'tvYearslh':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().years()

elif action == 'tvGenreslh':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().genres()

elif action == 'tvLanguageslh':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().languages()

elif action == 'tvCertificateslh':
    from resources.lib.indexers import lhtvshows
    lhtvshows.tvshows().certifications()

elif action == 'movieGenreslh':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().genres()
	
elif action == 'movieLanguageslh':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().languages()

elif action == 'movieCertificateslh':
    from resources.lib.indexers import lhmovies
    lhmovies.movies().certifications()
############################3wild west####################

elif action == 'gtmovNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().gtm()
	
elif action == 'gtmovGenres':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().genres()

elif action == 'gtmovLanguages':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().languages()

elif action == 'gtmovCertificates':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().certifications()

elif action == 'gtmovYears':
    from resources.lib.indexers import wwmovies
    wwmovies.movies().years()


elif action == 'gttvnav':
    from resources.lib.indexers import navigator
    navigator.navigator().gttv()

elif action == 'gttvYears':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().years()

elif action == 'gttvGenres':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().genres()

elif action == 'gttvLanguages':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().languages()


elif action == 'gttvCertificates':
    from resources.lib.indexers import wwtvshows
    wwtvshows.tvshows().certifications()


