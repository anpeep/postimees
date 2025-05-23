# Postimees Prompt Improver

This script allows you to iteratively improve a prompt using the OpenAI API. From an initial prompt and an improvement prompt it performs a given number of iterations where each response becomes the new prompt.


## Technologies Used

- **Python 3** - I choose it over PHP, Go and Typescript because of my familiarity with this language
- **OpenAI GPT model** – for generating and refining prompts
- **Custom Config File** – for securely loading your OpenAI API key from `config.py`



## Running Instructions

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. **Set up your environment**

Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## 3. **Configure API Key**

Add your OpenAI API key to __config.py__ file:

```
OPEN_AI_API_KEY = "your_openai_api_key_here"
```

## 4. Run the script

Run in terminal by:

```bash
py main.py
```
Script will ask your input for:

* Your initial prompt

* The improvement prompt

* Number of iterations

* The OpenAI model to use (e.g., gpt-3.5-turbo, gpt-4)

## 5. Example

Input:

```
Initial prompt: pirates are cool
Improvement prompt: make it more compelling
Iterations: 5
Model (e.g., gpt-3.5-turbo): gpt-4o-mini
```

Output of each iteration step-by-step and the final improved prompt.

```
--- Iteration 1 ---
Pirates are undeniably cool! They embody a spirit of adventure, rebellion, and freedom on the high seas. With their iconic ships, elaborate treasure maps, and tales of daring escapades, they ignite our imaginations and take us on thrilling journeys through history. From the infamous Blackbeard to the cunning Anne Bonny, each pirate has a story that fascinates us and draws us into their world of bold exploits and treacherous waters. The allure of buried treasure and the code of honor among rogues add layers of intrigue to their legacy. Plus, who doesn't love the romanticized image of a pirate with a weathered map, a parrot on their shoulder, and a hearty "Arrr!"? Pirates are not just figures of folklore; they represent a timeless quest for independence and adventure that resonates with the dreamer in all of us. So, let’s hoist the sails and embrace the thrilling lore of piracy!

--- Iteration 2 ---
Pirates are the quintessential embodiment of adventure, rebellion, and the unquenchable thirst for freedom on the high seas! With their majestic ships cutting through azure waves and the promise of treasure hidden beneath windswept islands, they capture our imaginations and whisk us away on heart-pounding escapades woven into the fabric of history. From the legendary Blackbeard, whose fierce reputation sent shivers down the spine of sailors, to the audacious Anne Bonny, whose daring exploits defied societal norms, each pirate carries with them a tale that grips our hearts and pulls us deeper into their world of audacity, charm, and danger.

The allure of buried treasure, the tantalizing whispers of the code of honor shared among rogues, and the thrill of a life lived on the edge all intertwine to create a compelling narrative that lingers in our dreams. Think of the swashbuckling figure with a weathered map clutched in one hand, a colorful parrot perched on their shoulder, and a raucous "Arrr!" echoing through the briny air. These images are not mere folklore; they represent a timeless quest for independence and adventure that resonates with the inner dreamer, the seeker of new horizons in all of us.

So, let us not just admire these daring souls from the comfort of our armchairs! Let us hoist the sails, embrace the siren call of piracy, and dive headfirst into a world filled with camaraderie, danger, and revelry on the open seas! The legend of the pirate beckons us to explore, to uncover hidden caches of valor, and to revel in the unyielding pursuit of freedom that fuels the human spirit! Join me, and let’s chart a course into the thrilling lore of piracy!

--- Iteration 3 ---
Pirates stand as the ultimate icons of adventure, rebellion, and an insatiable craving for freedom upon the boundless waves of the ocean! Picture, if you will, majestic ships slicing through brilliant azure waters, their sails billowing in the wind, as secrets of untold treasures lie concealed beneath windswept shores. These swashbuckling figures fire our imaginations and whisk us away on electrifying escapades intricately woven into the vibrant tapestry of history. From the fearsome Blackbeard, whose very name invoked terror among sailors, to the daring Anne Bonny, a trailblazer who shattered societal expectations, every pirate carries a story that grips our hearts and plunges us into a world of audacity, charm, and peril.

The magnetic allure of buried treasure, the tantalizing tales of a code of honor adhered to by rogues, and the intoxicating thrill of a life lived on the precipice converge to create a breathtaking narrative that resonates deeply within us. Envision the iconic figure, map in hand—its edges frayed and marks faded—while a vibrant parrot squawks from their shoulder, echoing a raucous "Arrr!" that dances joyfully on the salty breeze. These images are far from mere folklore; they represent a timeless desire for independence and adventure, a call to the inner dreamer and seeker of new horizons that resides in us all.

So let's not be mere spectators, admiring the audacious exploits of these daring souls from the safety of our armchairs! Let us hoist the sails, answer the intoxicating siren call of piracy, and plunge headfirst into a realm brimming with camaraderie, excitement, and revelry upon the open seas! The captivating saga of pirates invites us on a quest to explore the uncharted waters, to unearth hidden treasures of valor and rebellion, and to immerse ourselves in the unstoppable pursuit of freedom that ignites the human spirit! Join me, and let’s carve a path through the exhilarating lore of piracy—because the adventure of a lifetime awaits us on the horizon!

--- Iteration 4 ---
Pirates—the undaunted legends of the sea, the embodiment of adventure, rebellion, and an unquenchable thirst for freedom! Imagine, if you will, majestic ships gliding over crystalline azure waves, their sails billowing like thunderous wings, each vessel a floating testament to the mysteries of the deep. Beneath the sun-drenched shores, buried treasures lie in wait, their glittering secrets shrouded in the whispers of the wind. These bold rogues have captured our collective imagination, whisking us away on electrifying escapades intricately woven into the vibrant tapestry of history.

From the fearsome Blackbeard, whose very name sent waves of dread crashing through the hearts of mariners, to the audacious Anne Bonny, a fierce trailblazer who shattered the chains of societal norms, every pirate embodies a story that seizes our souls and propels us into a world of audacity, charisma, and danger. Each swashbuckling figure is a reminder of the allure of the unknown, the intoxicating blend of risk and reward that calls to the deepest corners of our hearts.

Feel the magnetic pull of buried treasure that sparkles with the promise of adventure! Envision the rogue captain, weathered map in hand—its edges frayed, ink bled by the relentless passage of time—as a brilliantly colored parrot squawks from their shoulder, sending a jubilant "Arrr!" cascading through the salty air. These images transcend mere folklore; they symbolize a timeless yearning for independence and the exhilaration of living on the edge—a clarion call to all dreamers and seekers of new horizons.

But why be mere spectators, peering at the exhilarating exploits of these fearless souls from the comfort of our couches? Let us raise our sails, heed the siren call of piracy, and dive wholeheartedly into a realm alive with camaraderie, thrill, and unfettered revelry upon the boundless seas! The captivating saga of piracy beckons us on a quest through uncharted waters, daring us to unearth treasures of valor, rebellion, and the relentless pursuit of freedom that ignites the human spirit.

Join me as we embark on a journey to navigate the exhilarating lore of piracy—where every wave carries a story, every storm holds a secret, and the horizon is a promise of an adventure unlike any other. Together, we’ll carve a path through the annals of piracy and discover that the adventure of a lifetime is not just on the horizon; it awaits us within the very fabric of our dreams! Let’s sail forth! 🌊🏴‍☠️✨

--- Iteration 5 ---
Pirates—the unyielding legends of the sea, the very essence of audacious adventure, rebellion, and an insatiable thirst for freedom! Picture, if you will, majestic ships cutting through crystalline azure waves, their sails unfurling like thunderous wings. Each vessel is a floating testament to the deep’s infinite mysteries, where untold stories lie just beneath the surface. Beneath the sun-kissed shores, glimmering treasures lie buried—guarded secrets yearning to be unearthed, their mystique enriched by the whispers of the wind and the tales of daring souls who've dared to seek them.

From the fearsome Blackbeard, whose name sent tremors of dread through the hearts of sailors, to the fierce and audacious Anne Bonny, a trailblazer who defied the very fabric of societal constraints, every pirate is a vibrant thread in the rich tapestry of history. They embody a narrative that seizes our imaginations, propelling us into a world brimming with charisma, danger, and extraordinary courage. Each swashbuckler reminds us of the allure of the unknown—the intoxicating fusion of risk and reward that ignites something deep within us all, summoning the dreamer and the adventurer alike.

Feel the magnetic pull of buried treasure that glints with the promise of adventure and the thrill of discovery! Envision the rogue captain, map in hand—its edges weathered and ink faded by the relentless march of time—as a brilliantly plumed parrot squawks joyfully from their shoulder, sending jubilant “Arrrs!” cascading through the salty air. These visions transcend mere folklore; they symbolize a timeless yearning for independence and the electrifying exhilaration of living life on one’s own terms—a clarion call to the dreamers and seekers who long for their own horizon.

But why remain mere spectators, peering enviously at the heart-pounding exploits of these daring souls from our cozy vantage points? Let us hoist our sails, embrace the siren call of piracy, and dive fearlessly into a realm vibrant with camaraderie, thrill, and unfettered celebration upon the vast seas! The enthralling saga of piracy invites us on a daring quest through uncharted waters, challenging us to unearth treasures of bravery, rebellion, and the relentless pursuit of freedom that fuels the human spirit.

Join me as we embark on an unforgettable odyssey to navigate the exhilarating lore of piracy—where every wave carries a tale, every tempest guards a secret, and the horizon holds the promise of adventures yet unfathomed. Together, we’ll carve a legendary path through the annals of this epic history and discover that the adventure of a lifetime is not merely waiting on the horizon; it pulses within the very fabric of our dreams, waiting for us to seize it! So, raise your cup of grog and let’s set sail! 🌊🏴‍☠️✨

=== Final Result ===
Prompt: Pirates—the unyielding legends of the sea, the very essence of audacious adventure, rebellion, and an insatiable thirst for freedom! Picture, if you will, majestic ships cutting through crystalline azure waves, their sails unfurling like thunderous wings. Each vessel is a floating testament to the deep’s infinite mysteries, where untold stories lie just beneath the surface. Beneath the sun-kissed shores, glimmering treasures lie buried—guarded secrets yearning to be unearthed, their mystique enriched by the whispers of the wind and the tales of daring souls who've dared to seek them.

From the fearsome Blackbeard, whose name sent tremors of dread through the hearts of sailors, to the fierce and audacious Anne Bonny, a trailblazer who defied the very fabric of societal constraints, every pirate is a vibrant thread in the rich tapestry of history. They embody a narrative that seizes our imaginations, propelling us into a world brimming with charisma, danger, and extraordinary courage. Each swashbuckler reminds us of the allure of the unknown—the intoxicating fusion of risk and reward that ignites something deep within us all, summoning the dreamer and the adventurer alike.

Feel the magnetic pull of buried treasure that glints with the promise of adventure and the thrill of discovery! Envision the rogue captain, map in hand—its edges weathered and ink faded by the relentless march of time—as a brilliantly plumed parrot squawks joyfully from their shoulder, sending jubilant “Arrrs!” cascading through the salty air. These visions transcend mere folklore; they symbolize a timeless yearning for independence and the electrifying exhilaration of living life on one’s own terms—a clarion call to the dreamers and seekers who long for their own horizon.

But why remain mere spectators, peering enviously at the heart-pounding exploits of these daring souls from our cozy vantage points? Let us hoist our sails, embrace the siren call of piracy, and dive fearlessly into a realm vibrant with camaraderie, thrill, and unfettered celebration upon the vast seas! The enthralling saga of piracy invites us on a daring quest through uncharted waters, challenging us to unearth treasures of bravery, rebellion, and the relentless pursuit of freedom that fuels the human spirit.

Join me as we embark on an unforgettable odyssey to navigate the exhilarating lore of piracy—where every wave carries a tale, every tempest guards a secret, and the horizon holds the promise of adventures yet unfathomed. Together, we’ll carve a legendary path through the annals of this epic history and discover that the adventure of a lifetime is not merely waiting on the horizon; it pulses within the very fabric of our dreams, waiting for us to seize it! So, raise your cup of grog and let’s set sail! 🌊🏴‍☠️✨
Iterations: 5
Model: gpt-4o-mini
```

