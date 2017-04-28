function preload() {

    game.stage.backgroundColor = '#85b5e1';

    game.load.baseURL = 'http://examples.phaser.io/assets/';
    game.load.crossOrigin = 'anonymous';

    game.load.image('player', 'sprites/phaser-dude.png');
    game.load.image('platform', 'http://www.debscrossstitch.co.uk/ekmps/shops/debscrossstitch/images/bright-blue-square-aperture-card-envelope-4-x-6-a6-bright-blue-square-aperture-4-x-6-5-x-cards-envelopes-1.85-2050-p.jpg');

}
var player;
var platforms;
var cursors;
var jumpButton;

function create() {

    player = game.add.sprite(400, 500, 'player');

    game.physics.arcade.enable(player);

    player.body.collideWorldBounds = true;
    
    platforms = game.add.physicsGroup();

    platforms.scale.setTo(2,1)
    platforms.create(80, 450, 'platform');
    platforms.create(180, 450, 'platform');
    platforms.create(290, 450, 'platform');

    platforms.setAll('body.immovable', true);

    cursors = game.input.keyboard.createCursorKeys();
    jumpButton = game.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);

}
function update () {

    game.physics.arcade.collide(player, platforms);

    player.body.velocity.x = 0;

    if (cursors.left.isDown)
    {
        player.body.velocity.x = -250;
    }
    else if (cursors.right.isDown)
    {
        player.body.velocity.x = 250;
    }

    if (jumpButton.isDown && (player.body.onFloor() || player.body.touching.down))
    {
        player.body.velocity.y = -400;
    }
}


//phaser.io/sandbox/XxhqEhZL