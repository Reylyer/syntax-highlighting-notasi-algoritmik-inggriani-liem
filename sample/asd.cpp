#ifndef _SCENE_INCLUDED
    #define _SCENE_INCLUDED

    #include "SceneObject.hpp"
    #include <map>
    #include <string>

    using   std::map,
            std::string;

    class Game;

    class Scene{
        public:
            map<string, SceneObject> objects;
            Game *game;
            bool is_active = false;
            string name;

        public:
            Scene(Game &game, string name);
            virtual void update();
        private:
            void render();
            void view();
    };
    // asd
    /* asd
    */
#endif

int main(){
    return asd;
}