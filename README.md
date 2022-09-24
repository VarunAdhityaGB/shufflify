
Authorization Scopes
====================

In order to use the Spotify Platform, you need to familiarise yourself with scopes. Scopes provide Spotify users using third-party apps the confidence that only the information they choose to share will be shared, and nothing more.

Overview
--------

*   Images
    *   [ugc-image-upload](#ugc-image-upload)
*   Spotify Connect
    *   [user-read-playback-state](#user-read-playback-state)
    *   [user-modify-playback-state](#user-modify-playback-state)
    *   [user-read-currently-playing](#user-read-currently-playing)
*   Playback
    *   [app-remote-control](#app-remote-control)
    *   [streaming](#streaming)
*   Playlists
    *   [playlist-read-private](#playlist-read-private)
    *   [playlist-read-collaborative](#playlist-read-collaborative)
    *   [playlist-modify-private](#playlist-modify-private)
    *   [playlist-modify-public](#playlist-modify-public)
*   Follow
    *   [user-follow-modify](#user-follow-modify)
    *   [user-follow-read](#user-follow-read)
*   Listening History
    *   [user-read-playback-position](#user-read-playback-position)
    *   [user-top-read](#user-top-read)
    *   [user-read-recently-played](#user-read-recently-played)
*   Library
    *   [user-library-modify](#user-library-modify)
    *   [user-library-read](#user-library-read)
*   Users
    *   [user-read-email](#user-read-email)
    *   [user-read-private](#user-read-private)

Scopes
------

### `ugc-image-upload`

**Description**

Write access to user-provided images.

**Visible to users**

Upload images to Spotify on your behalf.

**Endpoints that require the `ugc-image-upload` scope**

*   [Upload a Custom Playlist Cover Image](/documentation/web-api/reference/#/operations/upload-custom-playlist-cover)

### `user-read-playback-state`

**Description**

Read access to a user’s player state.

**Visible to users**

Read your currently playing content and Spotify Connect devices information.

**Endpoints that require the `user-read-playback-state` scope**

*   [Get a User's Available Devices](/documentation/web-api/reference/#/operations/get-a-users-available-devices)
*   [Get Information About The User's Current Playback](/documentation/web-api/reference/#/operations/get-information-about-the-users-current-playback)
*   [Get the User's Currently Playing Track](/documentation/web-api/reference/#/operations/get-recently-played)

### `app-remote-control`

**Description**

Remote control playback of Spotify. This scope is currently available to Spotify iOS and Android SDKs.

**Visible to users**

Communicate with the Spotify app on your device.

**Endpoints that require the `app-remote-control` scope**

*   [iOS SDK](/documentation/ios/)
*   [Android SDK](/documentation/android/)

### `user-modify-playback-state`

**Description**

Write access to a user’s playback state

**Visible to users**

Control playback on your Spotify clients and Spotify Connect devices.

**Endpoints that require the `user-modify-playback-state` scope**

*   [Pause a User's Playback](/documentation/web-api/reference/#/operations/pause-a-users-playback)
*   [Seek To Position In Currently Playing Track](/documentation/web-api/reference/#/operations/seek-to-position-in-currently-playing-track)
*   [Set Repeat Mode On User’s Playback](/documentation/web-api/reference/#/operations/set-repeat-mode-on-users-playback)
*   [Set Volume For User's Playback](/documentation/web-api/reference/#/operations/set-volume-for-users-playback)
*   [Skip User’s Playback To Next Track](/documentation/web-api/reference/#/operations/skip-users-playback-to-next-track)
*   [Skip User’s Playback To Previous Track](/documentation/web-api/reference/#/operations/skip-users-playback-to-previous-track)
*   [Start/Resume a User's Playback](/documentation/web-api/reference/#/operations/start-a-users-playback)
*   [Toggle Shuffle For User’s Playback](/documentation/web-api/reference/#/operations/toggle-shuffle-for-users-playback)
*   [Transfer a User's Playback](/documentation/web-api/reference/#/operations/transfer-a-users-playback)
*   [Add An Item To The End Of User's Current Playback Queue](/documentation/web-api/reference/#/operations/seek-to-position-in-currently-playing-track)

### `playlist-read-private`

**Description**

Read access to user's private playlists.

**Visible to users**

Access your private playlists.

**Endpoints that require the `playlist-read-private` scope**

*   [Check if Users Follow a Playlist](/documentation/web-api/reference/#/operations/check-if-user-follows-playlist)
*   [Get a List of Current User's Playlists](/documentation/web-api/reference/#/operations/get-a-list-of-current-users-playlists)
*   [Get a List of a User's Playlists](/documentation/web-api/reference/#/operations/get-list-users-playlists)

### `user-follow-modify`

**Description**

Write/delete access to the list of artists and other users that the user follows.

**Visible to users**

Manage who you are following.

**Endpoints that require the `user-follow-modify` scope**

*   [Follow Artists or Users](/documentation/web-api/reference/#/operations/follow-artists-users)
*   [Unfollow Artists or Users](/documentation/web-api/reference/#/operations/unfollow-artists-users)

### `playlist-read-collaborative`

**Description**

Include collaborative playlists when requesting a user's playlists.

**Visible to users**

Access your collaborative playlists.

**Endpoints that require the `playlist-read-collaborative` scope**

*   [Get a List of Current User's Playlists](/documentation/web-api/reference/#/operations/get-a-list-of-current-users-playlists)
*   [Get a List of a User's Playlists](/documentation/web-api/reference/#/operations/get-list-users-playlists)

### `user-follow-read`

**Description**

Read access to the list of artists and other users that the user follows.

**Visible to users**

Access your followers and who you are following.

**Endpoints that require the `user-follow-read` scope**

*   [Check if Current User Follows Artists or Users](/documentation/web-api/reference/#/operations/check-current-user-follows)
*   [Get User's Followed Artists](/documentation/web-api/#/operations/get-followed)

### `user-read-currently-playing`

**Description**

Read access to a user’s currently playing content.

**Visible to users**

Read your currently playing content.

**Endpoints that require the `user-read-currently-playing` scope**

*   [Get the User's Currently Playing Track](/documentation/web-api/reference/#/operations/get-recently-played)
*   [Get the User's Queue](/documentation/web-api/reference/#/operations/get-queue)

### `user-read-playback-position`

**Description**

Read access to a user’s playback position in a content.

**Visible to users**

Read your position in content you have played.

**Endpoints that require the `user-read-playback-position` scope**

*   [Get an Episodes](/documentation/web-api/reference/#/operations/get-an-episode)
*   [Get Several Episodes](/documentation/web-api/reference/#/operations/get-multiple-episodes)
*   [Get a Show](/documentation/web-api/reference/#/operations/get-a-show)
*   [Get Several Shows](/documentation/web-api/reference/#/operations/get-multiple-shows)
*   [Get a Show's Episodes](/documentation/web-api/reference/#/operations/get-a-shows-episodes)

### `user-library-modify`

**Description**

Write/delete access to a user's "Your Music" library.

**Visible to users**

Manage your saved content.

**Endpoints that require the `user-library-modify` scope**

*   [Remove Albums for Current User](/documentation/web-api/reference/#/operations/remove-albums-user)
*   [Remove User's Saved Tracks](/documentation/web-api/reference/#/operations/remove-tracks-user)
*   [Remove User's Saved Episodes](/documentation/web-api/reference/#/operations/remove-episodes-user)
*   [Save Albums for Current User](/documentation/web-api/reference/#/operations/save-albums-user)
*   [Save Tracks for User](/documentation/web-api/reference/#/operations/save-tracks-user)
*   [Save Episodes for User](/documentation/web-api/reference/#/operations/save-episodes-user)

### `playlist-modify-private`

**Description**

Write access to a user's private playlists.

**Visible to users**

Manage your private playlists.

**Endpoints that require the `playlist-modify-private` scope**

*   [Follow a Playlist](/documentation/web-api/reference/#/operations/follow-playlist)
*   [Unfollow a Playlist](/documentation/web-api/reference/#/operations/unfollow-playlist)
*   [Add Items to a Playlist](/documentation/web-api/reference/#/operations/add-tracks-to-playlist)
*   [Change a Playlist's Details](/documentation/web-api/reference/#/operations/change-playlist-details)
*   [Create a Playlist](/documentation/web-api/reference/#/operations/create-playlist)
*   [Remove Items from a Playlist](/documentation/web-api/reference/#/operations/remove-tracks-playlist)
*   [Reorder a Playlist's Items](/documentation/web-api/reference/#/operations/reorder-or-replace-playlists-tracks)
*   [Replace a Playlist's Items](/documentation/web-api/reference/#/operations/reorder-or-replace-playlists-tracks)
*   [Upload a Custom Playlist Cover Image](/documentation/web-api/reference/#/operations/upload-custom-playlist-cover)

### `playlist-modify-public`

**Description**

Write access to a user's public playlists.

**Visible to users**

Manage your public playlists.

**Endpoints that require the `playlist-modify-public` scope**

*   [Follow a Playlist](/documentation/web-api/reference/#/operations/follow-playlist)
*   [Unfollow a Playlist](/documentation/web-api/reference/#/operations/unfollow-playlist)
*   [Add Items to a Playlist](/documentation/web-api/reference/#/operations/add-tracks-to-playlist)
*   [Change a Playlist's Details](/documentation/web-api/reference/#/operations/change-playlist-details)
*   [Create a Playlist](/documentation/web-api/reference/#/operations/create-playlist)
*   [Remove Items from a Playlist](/documentation/web-api/reference/#/operations/remove-tracks-playlist)
*   [Reorder a Playlist's Items](/documentation/web-api/reference/#/operations/reorder-or-replace-playlists-tracks)
*   [Replace a Playlist's Items](/documentation/web-api/reference/#/operations/reorder-or-replace-playlists-tracks)
*   [Upload a Custom Playlist Cover Image](/documentation/web-api/reference/#/operations/upload-custom-playlist-cover)

### `user-read-email`

**Description**

Read access to user’s email address.

**Visible to users**

Get your real email address.

**Endpoints that require the `user-read-email` scope**

*   [Get Current User's Profile](/documentation/web-api/reference/#/operations/get-current-users-profile)

### `user-top-read`

**Description**

Read access to a user's top artists and tracks.

**Visible to users**

Read your top artists and content.

**Endpoints that require the `user-top-read` scope**

*   [Get a User's Top Artists and Tracks](/documentation/web-api/reference/#/operations/get-users-top-artists-and-tracks)

### `streaming`

**Description**

Control playback of a Spotify track. This scope is currently available to the Web Playback SDK. The user must have a Spotify Premium account.

**Visible to users**

Play content and control playback on your other devices.

**Endpoints that require the `streaming` scope**

*   [Web Playback SDK](/documentation/web-playback-sdk/)

### `user-read-recently-played`

**Description**

Read access to a user’s recently played tracks.

**Visible to users**

Access your recently played items.

**Endpoints that require the `user-read-recently-played` scope**

*   [Get Current User's Recently Played Tracks](/documentation/web-api/reference/#/operations/get-the-users-currently-playing-track)

### `user-read-private`

**Description**

Read access to user’s subscription details (type of user account).

**Visible to users**

Access your subscription details.

**Endpoints that require the `user-read-private` scope**

*   [Search for an Item](/documentation/web-api/reference/#/operations/search)
*   [Get Current User's Profile](/documentation/web-api/reference/#/operations/get-current-users-profile)

### `user-library-read`

**Description**

Read access to a user's library.

**Visible to users**

Access your saved content.

**Endpoints that require the `user-library-read` scope**

*   [Check User's Saved Albums](/documentation/web-api/reference/#/operations/check-users-saved-albums)
*   [Check User's Saved Tracks](/documentation/web-api/reference/#/operations/check-users-saved-tracks)
*   [Get Current User's Saved Albums](/documentation/web-api/reference/#/operations/get-users-saved-albums)
*   [Get a User's Saved Tracks](/documentation/web-api/reference/#/operations/get-users-saved-tracks)
*   [Check User's Saved Episodes](/documentation/web-api/reference/#/operations/check-users-saved-episodes)
*   [Get User's Saved Episodes](/documentation/web-api/reference/#/operations/get-users-saved-episodes)
