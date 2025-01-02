const player = OvenPlayer.create('player_id', {
    sources: [
        {
            label: 'label_for_webrtc',
            type: 'webrtc',
            file: 'ws://aramjonghu.nl:3333/app/stream'
        }
    ]
});