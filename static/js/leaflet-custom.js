$(document).ready(function() {
    if (document.getElementById("map") !== null) {
        if ($('#map').attr('data-map-scroll') == 'true' || $(window).width() < 992) { var scrollEnabled = false; } else { var scrollEnabled = true; }
        var mapOptions = { gestureHandling: scrollEnabled, }
        window.map = L.map('map', mapOptions);
        $('#scrollEnabling').hide();

        function locationData(locationURL, locationImg, locationTitle, locationCat, locationRating, locationReview) {
            return ('' +
                    '<div class="marker_info" id="marker_info">' +
                '<img src="' + locationImg + '" alt="..."/>' +
                '<span>'+ 
                    '<em>'+ locationCat +'</em>' +
                    '<h3><a href="'+locationURL+'">'+ locationTitle +'</a></h3>' +
                    '<span class="infobox_rate">'+ locationRating +'</span>' +
                    '<span class="btn_infobox_reviews">'+ locationReview + ' reviews</span>' +
                    '</span>' +
                '</div>'
                )
        }
        var infoBox_ratingType = 'star-rating';
        map.on('popupopen', function() {
            if (infoBox_ratingType = 'numerical-rating') { numericalRating('.leaflet-popup .' + infoBox_ratingType + ''); }
            if (infoBox_ratingType = 'star-rating') { starRating('.leaflet-popup .' + infoBox_ratingType + ''); }
        });
        var locations = [
            [locationData('single-listing-one.html', 'images/single-listing/gallery-6.jpg', "Ocean Paradise", 'Hotel', '4.5', '13'), 48.866024, 2.340041],

            [locationData('single-listing-two.html', 'images/category/places/place-5.jpg', 'Lagon Theme Park', 'Travel', '4', '12'), 48.868560, 2.349427],

            [locationData('single-listing-three.html', 'images/category/places/place-9.jpg', 'Genji Restaurent', 'Restaurent', '5', '11'), 48.870824, 2.333005],

            [locationData('single-listing-four.html', 'images/category/places/place-5.jpg', 'Lagon Theme Park', 'Travel', '3.5', '10'), 48.864642, 2.345837],

            [locationData('single-listing-five.html', 'images/category/places/cafe.jpg', 'Cafe Intermezzo', 'Caffee', '4.5', '9'), 48.861753, 2.338402],

            [locationData('single-listing-one.html', 'images/category/places/place-1.jpg', 'Four Seasons Resort', 'Hotel', '5', '8'), 48.872111, 2.345151],

            [locationData('single-listing-two.html', 'images/category/places/place-11.jpg', 'The Straling', 'Hotel', '4', '14'), 48.865881, 2.341507],

            [locationData('single-listing-two.html', 'images/category/event/muay.jpg', 'Muay Live Show', 'Event', '4', '15'),  48.867236, 2.343610]
        ];
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}@2x.png?access_token={accessToken}', { attribution: " &copy;  <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> &copy;  <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a>", maxZoom: 18, id: 'mapbox.streets', accessToken: 'pk.eyJ1IjoidmFzdGVyYWQiLCJhIjoiY2p5cjd0NTc1MDdwaDNtbnVoOGwzNmo4aSJ9.BnYb645YABOY2G4yWAFRVw' }).addTo(map);
        markers = L.markerClusterGroup({ spiderfyOnMaxZoom: true, showCoverageOnHover: false, });
        for (var i = 0; i < locations.length; i++) {
            var listagramIcon = L.divIcon({
                iconAnchor: [20, 51],
                popupAnchor: [0, -51],
                className: 'listagram-marker-icon',
                html: '<div class="marker-container">' +
                    '<div class="marker-card">' +
                    '<img src="images/others/marker.png" alt="..."/>' +
                    '</div>' +
                    '</div>'
            });
            var popupOptions = { 'maxWidth': '240', 'className': 'leaflet-infoBox' }
            var markerArray = [];
            marker = new L.marker([locations[i][1], locations[i][2]], { icon: listagramIcon, }).bindPopup(locations[i][0], popupOptions);
            marker.on('click', function(e) {});
            map.on('popupopen', function(e) { L.DomUtil.addClass(e.popup._source._icon, 'clicked'); }).on('popupclose', function(e) { if (e.popup) { L.DomUtil.removeClass(e.popup._source._icon, 'clicked'); } });
            markers.addLayer(marker);
        }
        map.addLayer(markers);
        markerArray.push(markers);
        if (markerArray.length > 0) { map.fitBounds(L.featureGroup(markerArray).getBounds().pad(0.2)); }
        map.removeControl(map.zoomControl);
        var zoomOptions = { zoomInText: '<i class="ion-plus" aria-hidden="true"></i>', zoomOutText: '<i class="ion-minus" aria-hidden="true"></i>', };
        var zoom = L.control.zoom(zoomOptions);
        zoom.addTo(map);
    }

   
});