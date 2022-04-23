var app = new Vue({
  el: "#app",
  data: {
    state: {
      latestcommit: null,
      modalData: null,
      maps: null,
    },
    events: [
      {
        id: 1,
        title: "Costume-themed Streets",
        body: `Victorian West Street, Edwardian High Street, Elizabethan Old Schools, and the Church. With many thanks to the members of the Harrow on the Hill Women's Institute for the more than 600m of wonderful handmade bunting and to the boys of Harrow School for all the flags.`,
        times: "3.30pm, 5.15pm", //could be an array of datetimes later
        location: 11,
        classification: "Events",
      },
      {
        id: 2,
        title: "Harrow Hill Trust Guided Walk",
        body: `A guided walk through Harrow Hill, with a focus on the history of the town and the Harrow Hill Trust. The walk will be led by a Harrow Hill Trust volunteer and will take approximately 1.5 hours.`,
        times: "3.30pm, 5.15pm",
        location: 19,
        classification: "Events",
      },
      {
        id: 2,
        title: "Food Market",
        body: `<p>Food stalls run by London's Community Kitchen will be serving a vast array of food and drink along the High Street between Moretons and Bradbys boarding houses.
      <p>
      <p>
      <ul>
        <li>The Kind Café</li>
        <li>Chipsy (Grilled burgers and loaded chips)</li>
        <li>Brat Bros Catering (Bratwurst, hot dogs, schnitzels)</li>
        <li>Sugo Kitchen (Italian Street Food, focaccia sandwiches, handmade pasta bowls)</li>
        <li>Gully (Indian Street Food) </li>
        <li>The Cheese Toaster (Gourmet cheese toasties)</li>
        <li>Social Dhaba (Punjabi Street Food)</li>
        <li>Paella Shack (Paella)</li>
        <li>Letterbox Cookie (Handmade cookies)</li>
        <li>Lilibet’s of Windsor (Traditional Old-Fashioned sweets)</li>
        <li>1218 Plant Based Cuisine (Vegan Street Food, salad boxes, BBQ and vegan sweet treats)</li>
        <li>Ben’s Bakery (Artisan Cakes)</li>
      </ul>
      </p>
      `,
        times: "noon – 6pm",
        location: 17,
        classification: "Food",
      },
    ],
    locations: {
      1: {
        title: "The Castle",
        coords: {
          lat: 51.5721,
          lng: -0.34,
        },
        icon: "./assets/icons/music.png",
      },
      2: {
        title: "The Band Stand",
        coords: {
          lat: 51.570709547070194,
          lng: -0.33953382679834193,
        },
        icon: "./assets/icons/music.png",
      },
      3: {
        title: "The Park Drive",
        coords: {
          lat: 51.57107799697978,
          lng: -0.33864699551627864,
        },
        icon: "./assets/icons/drama.png",
      },
      4: {
        title: "The Roof Terrace",
        coords: {
          lat: 51.572615028201376,
          lng: -0.3381793112539503,
        },
        icon: "./assets/icons/music.png",
      },
      5: {
        title: "The Old House",
        coords: {
          lat: 51.572306622419745,
          lng: -0.337707242462523,
        },
        icon: "./assets/icons/drama.png",
      },
      6: {
        title: "Speech Room",
        coords: {
          lat: 51.57388032088066,
          lng: -0.3365924234147868,
        },
        icon: "./assets/icons/drama.png",
      },
      7: {
        title: "Vaughan Library “Forecourt”",
        coords: {
          lat: 51.5729784615626,
          lng: -0.33683114001183134,
        },
        icon: "./assets/icons/drama.png",
      },
      8: {
        title: "Behind the Vaughan",
        coords: {
          lat: 51.57288677430271,
          lng: -0.3364073509924032,
        },
        icon: "./assets/icons/drama.png",
      },
      9: {
        title: "The Head Master’s Yard",
        coords: {
          lat: 51.57256920155196,
          lng: -0.33677481362631606,
        },
        icon: "./assets/icons/drama.png",
      },
      10: {
        title: "War Memorial Building Forecourt",
        coords: {
          lat: 51.57334270818231,
          lng: -0.3370028013856397,
        },
        icon: "./assets/icons/drama.png",
      },
      11: {
        title: "Bill Yard",
        coords: {
          lat: 51.57317433825023,
          lng: -0.3374212259876906,
        },
        icon: "./assets/icons/music.png",
      },
      12: {
        title: "Druries Steps",
        coords: {
          lat: 51.572975960994754,
          lng: -0.3373541707638017,
        },
        icon: "./assets/icons/drama.png",
      },
      13: {
        title: "Art Schools",
        coords: {
          lat: 51.57465043293017,
          lng: -0.33585118104491185,
        },
        icon: "./assets/icons/arts.png",
      },
      14: {
        title: "Passmore Gallery",
        coords: {
          lat: 51.5741953456611,
          lng: -0.3362347369255564,
        },
        icon: "./assets/icons/arts.png",
      },
      15: {
        title: "Grove Hill Portaloos",
        coords: {
          lat: 51.573988106438506,
          lng: -0.33615847667901955,
        },
        icon: "./assets/icons/wc.png",
      },
      16: {
        title: "Harrow Park Portaloos",
        coords: {
          lat: 51.56982528515575,
          lng: -0.3391569089820675,
        },
        icon: "./assets/icons/wc.png",
      },
      17: {
        title: "London Community Kitchen",
        coords: {
          lat: 51.57150259260376,
          lng: -0.33864416430660427,
        },
        icon: "./assets/icons/food.png",
      },
      18: {
        title: "Picnic Area",
        coords: {
          lat: 51.572578688703,
          lng: -0.3376919801021046,
        },
        icon: "./assets/icons/picnic.png",
      },
      19: {
        title: "St Mary's",
        coords: {
          lat: 51.574059316831075,
          lng: -0.3371416801004325,
        },
        icon: "./assets/icons/arts.png",
      },
    },
  },
  methods: {
    dateformat(input) {
      return new Date(input).toLocaleDateString('en-GB', {
          year: 'numeric',
          month: '2-digit',
          day: '2-digit',
          hour:'2-digit',
          minute:'2-digit'
      });
  },
    modalOpened() {
      if (this.state.maps) {
        this.state.maps.remove();
      }

      var button = event.relatedTarget;
      var locationid = button.getAttribute("data-bs-locationid");

      var location = this.locations[locationid];

      this.state.maps = L.map("mainMap" + locationid);

      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZHlsYW5rMTIzIiwiYSI6ImNrajUwMm55NzV0NWwyc2xiNzk0OHFjdXoifQ.cIzWvi9HlI1YfhpY24KbTA",
        {
          maxZoom: 18,
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          id: "dylank123/ckl2u73iy1s5v17tjzyld3nzl",
          tileSize: 512,
          zoomOffset: -1,
        }
      ).addTo(this.state.maps);

      var icon = L.icon({
        iconUrl: location.icon,
        //shadowUrl: 'leaf-shadow.png',

        iconSize: [25, 25], // size of the icon
        // shadowSize:   [50, 64], // size of the shadow
        // iconAnchor:   [12.5, 12.5], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor:  [12.5, 12.5] // point from which the popup should open relative to the iconAnchor
      });

      var marker = L.marker([location.coords.lat, location.coords.lng], {
        icon: icon,
      })
        .addTo(this.state.maps)
        .bindPopup(location.title);

      this.state.maps.setView([location.coords.lat, location.coords.lng], 17);

      this.state.maps.invalidateSize();
    },
  },
  mounted() {


      axios
        .get('https://api.github.com/repos/harrowschool/harrowschool.github.io/commits?per_page=1')
        .then(response => (this.state.latestcommit = response.data[0]))



    var mainMap = L.map("mainMap");

    window.addEventListener("show.bs.modal", this.modalOpened);

    L.tileLayer(
      "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZHlsYW5rMTIzIiwiYSI6ImNrajUwMm55NzV0NWwyc2xiNzk0OHFjdXoifQ.cIzWvi9HlI1YfhpY24KbTA",
      {
        maxZoom: 18,
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: "dylank123/ckl2u73iy1s5v17tjzyld3nzl",
        tileSize: 512,
        zoomOffset: -1,
      }
    ).addTo(mainMap);

    Object.values(this.locations).forEach((location) => {
      var icon = L.icon({
        iconUrl: location.icon,
        //shadowUrl: 'leaf-shadow.png',

        iconSize: [25, 25], // size of the icon
        // shadowSize:   [50, 64], // size of the shadow
        // iconAnchor:   [12.5, 12.5], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor:  [12.5, 12.5] // point from which the popup should open relative to the iconAnchor
      });

      var marker = L.marker([location.coords.lat, location.coords.lng], {
        icon: icon,
      })
        .addTo(mainMap)
        .bindPopup(location.title);
    });

    mainMap.setView([51.57281743898807, -0.3371716811246794], 17);

    // shows user's location on map
    // function onLocationFound(e) {
    //     var radius = e.accuracy / 2;

    //     var locationMarker = L.marker(e.latlng).addTo(mymap)
    //         .bindPopup('You are within ' + radius + ' meters from this point').openPopup();

    //     var locationCircle = L.circle(e.latlng, radius).addTo(mymap);
    // }

    // function onLocationError(e) {
    //     alert(e.message);
    // }

    // mymap.on('locationfound', onLocationFound);
    // mymap.on('locationerror', onLocationError);

    // mymap.locate({ setView: true, maxZoom: 16 });
  },
});
